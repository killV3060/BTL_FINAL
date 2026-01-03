"""
Code Generator for OPLang programming language.
This module implements a code generator that traverses AST nodes and generates
Java bytecode using the Emitter and Frame classes.
"""

from typing import Any, List, Optional, Union
from ..utils.visitor import ASTVisitor
from ..utils.nodes import *
from .emitter import Emitter, is_void_type, is_int_type, is_string_type, is_bool_type, is_float_type
from .frame import Frame
from .error import IllegalOperandException, IllegalRuntimeException
from .io import IO_SYMBOL_LIST
from .utils import *
from functools import *


class CodeGenerator(ASTVisitor):
    """
    Code generator for OPLang.
    Traverses AST and generates JVM bytecode.
    """
    
    def __init__(self):
        self.current_class = None
        self.emit = None  # Will be initialized per class

    # ============================================================================
    # Program and Class Declarations
    # ============================================================================

    def visit_program(self, node: "Program", o: Any = None):
        """
        Visit program node - generate code for all classes.
        """
        # Process all class declarations
        for class_decl in node.class_decls:
            self.visit(class_decl, o)

    def visit_class_decl(self, node: "ClassDecl", o: Any = None):
        """
        Visit class declaration - generate class structure.
        """
        self.current_class = node.name
        class_file = node.name + ".j"
        self.emit = Emitter(class_file)
        
        # Determine superclass
        superclass = node.superclass if node.superclass else "java/lang/Object"
        
        # Emit class prolog
        self.emit.print_out(self.emit.emit_prolog(node.name, superclass))
        
        # Process class members (attributes, methods, constructors, destructors)
        for member in node.members:
            self.visit(member, o)
        
        # Emit class epilog
        self.emit.emit_epilog()

    # ============================================================================
    # Attribute Declarations
    # ============================================================================

    def visit_attribute_decl(self, node: "AttributeDecl", o: Any = None):
        """
        Visit attribute declaration - generate field directives.
        TODO: Implement attribute initialization if needed
        """
        for attr in node.attributes:
            self.visit(attr, node)

    def visit_attribute(self, node: "Attribute", o: Any = None):
        """
        Visit individual attribute - generate field directive.
        """
        attr_decl = o  # AttributeDecl node
        class_name = self.current_class
        field_name = class_name + "/" + node.name
        
        # Emit field directive
        if attr_decl.is_static:
            self.emit.print_out(
                self.emit.emit_attribute(
                    field_name,
                    attr_decl.attr_type,
                    attr_decl.is_final
                )
            )
        else:
            # Instance field
            self.emit.print_out(
                self.emit.jvm.emitINSTANCEFIELD(
                    field_name,
                    self.emit.get_jvm_type(attr_decl.attr_type)
                )
            )
        
        # TODO: Handle initialization if node.init_value is not None

    # ============================================================================
    # Method Declarations
    # ============================================================================

    def visit_method_decl(self, node: "MethodDecl", o: Any = None):
        """
        Visit method declaration - generate method code.
        """
        frame = Frame(node.name, node.return_type)
        self.generate_method(node, frame, node.is_static)

    def visit_constructor_decl(self, node: "ConstructorDecl", o: Any = None):
        """
        Visit constructor declaration - generate constructor code.
        """
        frame = Frame("<init>", PrimitiveType("void"))
        self.generate_method(node, frame, False, is_constructor=True)

    def visit_destructor_decl(self, node: "DestructorDecl", o: Any = None):
        """
        Visit destructor declaration - generate destructor code.
        """
        frame = Frame("~" + self.current_class, PrimitiveType("void"))
        self.generate_method(node, frame, False)

    def visit_parameter(self, node: "Parameter", o: Any = None):
        """
        Visit parameter - register parameter in frame.
        """
        # This is handled in generate_method
        pass

    def generate_method(self, node: Union["MethodDecl", "ConstructorDecl", "DestructorDecl"], frame: Frame, is_static: bool, is_constructor: bool = False):
        """
        Generate code for a method.
        
        Args:
            node: Method or constructor/destructor declaration node
            frame: Frame for this method
            is_static: Whether method is static
            is_constructor: Whether this is a constructor
        """
        class_name = self.current_class
        method_name = "<init>" if is_constructor else node.name
        
        # Build method signature
        if isinstance(node, (MethodDecl, ConstructorDecl)):
            param_types = [p.param_type for p in node.params]
        else:
            param_types = []
            
        return_type = node.return_type if isinstance(node, MethodDecl) else PrimitiveType("void")
        
        # OPLang main method to Java main method mapping
        actual_method_name = method_name
        actual_func_type = FunctionType(param_types, return_type)
        if method_name == "main" and is_static:
            actual_method_name = "main"
            actual_func_type = FunctionType([ArrayType(PrimitiveType("string"), 0)], PrimitiveType("void"))
        
        # Emit method directive
        self.emit.print_out(
            self.emit.emit_method(
                actual_method_name,
                actual_func_type,
                is_static
            )
        )
        
        frame.enter_scope(True)
        from_label = frame.get_start_label()
        to_label = frame.get_end_label()
        
        sym_list = []
        # Handle 'this' parameter for instance methods
        if not is_static:
            this_idx = frame.get_new_index()
            self.emit.print_out(
                self.emit.emit_var(
                    this_idx,
                    "this",
                    ClassType(class_name),
                    from_label,
                    to_label
                )
            )
            # Add 'this' to symbol list
            sym_list.append(Symbol("this", ClassType(class_name), Index(this_idx)))
        elif method_name == "main":
            # Reserve index for String[] args
            frame.get_new_index()
        
        # Generate code for parameters
        if isinstance(node, (MethodDecl, ConstructorDecl)):
            for i, param in enumerate(node.params):
                idx = frame.get_new_index()
                self.emit.print_out(
                    self.emit.emit_var(
                        idx,
                        param.name,
                        param.param_type,
                        from_label,
                        to_label
                    )
                )
                sym_list.append(Symbol(param.name, param.param_type, Index(idx)))
        
        # Add IO symbols
        sym_list = IO_SYMBOL_LIST + sym_list
        
        self.emit.print_out(self.emit.emit_label(from_label, frame))
        
        if is_constructor:
            # Call super constructor
            self.emit.print_out(self.emit.emit_read_var("this", ClassType(class_name), 0, frame))
            self.emit.print_out(self.emit.emit_invoke_special(frame, "java/lang/Object/<init>", FunctionType([], PrimitiveType("void"))))

        # Generate code for method body
        o = SubBody(frame, sym_list)
        self.visit(node.body, o)
        
        # Emit return if void
        if is_void_type(return_type):
            self.emit.print_out(self.emit.emit_return(return_type, frame))
        
        self.emit.print_out(self.emit.emit_label(to_label, frame))
        self.emit.print_out(self.emit.emit_end_method(frame))
        
        frame.exit_scope()

    # ============================================================================
    # Type System
    # ============================================================================

    def visit_primitive_type(self, node: "PrimitiveType", o: Any = None):
        pass

    def visit_array_type(self, node: "ArrayType", o: Any = None):
        pass

    def visit_class_type(self, node: "ClassType", o: Any = None):
        pass

    def visit_reference_type(self, node: "ReferenceType", o: Any = None):
        pass

    # ============================================================================
    # Statements
    # ============================================================================

    def visit_block_statement(self, node: "BlockStatement", o: SubBody = None):
        """
        Visit block statement - process variable declarations and statements.
        """
        if o is None:
            return
        
        # Process variable declarations
        for var_decl in node.var_decls:
            o = self.visit(var_decl, o)
        
        # Process statements
        for stmt in node.statements:
            self.visit(stmt, o)

    def visit_variable_decl(self, node: "VariableDecl", o: SubBody = None):
        """
        Visit variable declaration - register local variables.
        """
        if o is None:
            return o
        
        frame = o.frame
        from_label = frame.get_start_label()
        to_label = frame.get_end_label()
        
        new_sym = []
        for var in node.variables:
            idx = frame.get_new_index()
            self.emit.print_out(
                self.emit.emit_var(
                    idx,
                    var.name,
                    node.var_type,
                    from_label,
                    to_label
                )
            )
            
            # Add to symbol list
            new_sym.append(Symbol(var.name, node.var_type, Index(idx)))
            
            # Handle initialization if present
            if var.init_value is not None:
                # Generate code for initialization
                code, typ = self.visit(var.init_value, Access(frame, o.sym))
                self.emit.print_out(code)
                self.emit.print_out(
                    self.emit.emit_write_var(var.name, node.var_type, idx, frame)
                )
        
        return SubBody(frame, new_sym + o.sym)

    def visit_variable(self, node: "Variable", o: Any = None):
        pass

    def visit_assignment_statement(self, node: "AssignmentStatement", o: SubBody = None):
        """
        Visit assignment statement - generate assignment code.
        """
        if o is None:
            return
        
        # Generate code for RHS
        code, typ = self.visit(node.rhs, Access(o.frame, o.sym))
        self.emit.print_out(code)
        
        # Generate code for LHS
        lhs_code, lhs_type = self.visit(node.lhs, Access(o.frame, o.sym, is_left=True))
        self.emit.print_out(lhs_code)

    def visit_if_statement(self, node: "IfStatement", o: SubBody = None):
        """
        Visit if statement.
        """
        if o is None:
            return
        frame = o.frame
        # condition
        code, typ = self.visit(node.condition, Access(frame, o.sym))
        self.emit.print_out(code)
        
        false_label = frame.get_new_label()
        exit_label = frame.get_new_label()
        
        self.emit.print_out(self.emit.emit_if_false(false_label, frame))
        self.visit(node.then_stmt, o)
        self.emit.print_out(self.emit.emit_goto(exit_label, frame))
        self.emit.print_out(self.emit.emit_label(false_label, frame))
        if node.else_stmt:
            self.visit(node.else_stmt, o)
        self.emit.print_out(self.emit.emit_label(exit_label, frame))

    def visit_for_statement(self, node: "ForStatement", o: SubBody = None):
        """
        Visit for statement.
        """
        if o is None:
            return
        frame = o.frame
        # Find loop variable
        sym = next(filter(lambda x: x.name == node.variable, o.sym), None)
        idx = sym.value.value
        
        # init: var := start_expr
        code, typ = self.visit(node.start_expr, Access(frame, o.sym))
        self.emit.print_out(code)
        self.emit.print_out(self.emit.emit_write_var(node.variable, typ, idx, frame))
        
        frame.enter_loop()
        start_label = frame.get_continue_label()
        exit_label = frame.get_break_label()
        
        self.emit.print_out(self.emit.emit_label(start_label, frame))
        
        # condition: var <= end_expr (to) or var >= end_expr (downto)
        self.emit.print_out(self.emit.emit_read_var(node.variable, typ, idx, frame))
        end_code, end_typ = self.visit(node.end_expr, Access(frame, o.sym))
        self.emit.print_out(end_code)
        
        if node.direction == "to":
            self.emit.print_out(self.emit.emit_rel_op("<=", typ, -1, exit_label, frame))
        else:
            self.emit.print_out(self.emit.emit_rel_op(">=", typ, -1, exit_label, frame))
            
        self.visit(node.body, o)
        
        # update: var := var + 1 or var - 1
        self.emit.print_out(self.emit.emit_read_var(node.variable, typ, idx, frame))
        self.emit.print_out(self.emit.emit_push_iconst(1, frame))
        if node.direction == "to":
            self.emit.print_out(self.emit.emit_add_op("+", PrimitiveType("int"), frame))
        else:
            self.emit.print_out(self.emit.emit_add_op("-", PrimitiveType("int"), frame))
        self.emit.print_out(self.emit.emit_write_var(node.variable, typ, idx, frame))
        
        self.emit.print_out(self.emit.emit_goto(start_label, frame))
        self.emit.print_out(self.emit.emit_label(exit_label, frame))
        frame.exit_loop()

    def visit_break_statement(self, node: "BreakStatement", o: SubBody = None):
        """
        Visit break statement.
        """
        if o is None:
            return
        self.emit.print_out(self.emit.emit_goto(o.frame.get_break_label(), o.frame))

    def visit_continue_statement(self, node: "ContinueStatement", o: SubBody = None):
        """
        Visit continue statement.
        """
        if o is None:
            return
        self.emit.print_out(self.emit.emit_goto(o.frame.get_continue_label(), o.frame))

    def visit_return_statement(self, node: "ReturnStatement", o: SubBody = None):
        """
        Visit return statement - generate return code.
        """
        if o is None:
            return
        
        # Generate code for return value
        code, typ = self.visit(node.value, Access(o.frame, o.sym))
        self.emit.print_out(code)
        
        # Emit return instruction
        self.emit.print_out(self.emit.emit_return(typ, o.frame))

    def visit_method_invocation_statement(
        self, node: "MethodInvocationStatement", o: SubBody = None
    ):
        """
        Visit method invocation statement.
        """
        if o is None:
            return
        code, typ = self.visit(node.method_call, Access(o.frame, o.sym))
        self.emit.print_out(code)
        if not is_void_type(typ):
            self.emit.print_out(self.emit.emit_pop(o.frame))

    # ============================================================================
    # Left-hand Side (LHS)
    # ============================================================================

    def visit_id_lhs(self, node: "IdLHS", o: Access = None):
        """
        Visit identifier LHS - generate code to write to variable.
        """
        if o is None:
            return "", None
        
        # Find symbol
        sym = next(filter(lambda x: x.name == node.name, o.sym), None)
        if sym is None:
            raise IllegalOperandException(f"Undeclared variable: {node.name}")
        
        if type(sym.value) is Index:
            code = self.emit.emit_write_var(
                sym.name, sym.type, sym.value.value, o.frame
            )
            return code, sym.type
        else:
            raise IllegalOperandException(f"Cannot assign to: {node.name}")

    def visit_postfix_lhs(self, node: "PostfixLHS", o: Access = None):
        """
        Visit postfix LHS (for member access, array access).
        """
        if o is None:
            return "", None
        
        # We need to generate code for the receiver and indices
        # but NOT the final store instruction, which visit_assignment_statement does
        # This is tricky because visit_postfix_expression usually generates Loads.
        # Let's assume visit_postfix_expression with is_left=True handles it.
        return self.visit(node.postfix_expr, o)

    # ============================================================================
    # Expressions
    # ============================================================================

    def visit_binary_op(self, node: "BinaryOp", o: Access = None):
        """
        Visit binary operation.
        """
        if o is None:
            return "", None
        lc, lt = self.visit(node.left, o)
        rc, rt = self.visit(node.right, o)
        
        # Simplified type promotion logic
        res_type = PrimitiveType("float") if is_float_type(lt) or is_float_type(rt) else PrimitiveType("int")
        
        code = lc
        if is_float_type(res_type) and is_int_type(lt):
            code += self.emit.emit_i2f(o.frame)
        code += rc
        if is_float_type(res_type) and is_int_type(rt):
            code += self.emit.emit_i2f(o.frame)
            
        op = node.operator
        if op in ["+", "-"]:
            code += self.emit.emit_add_op(op, res_type, o.frame)
            return code, res_type
        elif op in ["*", "/"]:
            code += self.emit.emit_mul_op(op, res_type, o.frame)
            return code, res_type
        elif op == "%":
            code += self.emit.emit_mod(o.frame)
            return code, PrimitiveType("int")
        elif op == "&&":
            code += self.emit.emit_and_op(o.frame)
            return code, PrimitiveType("boolean")
        elif op == "||":
            code += self.emit.emit_or_op(o.frame)
            return code, PrimitiveType("boolean")
        elif op in [">", ">=", "<", "<=", "==", "!="]:
            # Use LT type for relational ops before promotion to boolean
            code += self.emit.emit_re_op(op, res_type, o.frame)
            return code, PrimitiveType("boolean")
        
        return code, res_type

    def visit_unary_op(self, node: "UnaryOp", o: Access = None):
        """
        Visit unary operation.
        """
        if o is None:
            return "", None
        code, typ = self.visit(node.operand, o)
        if node.operator == "-":
            code += self.emit.emit_neg_op(typ, o.frame)
        elif node.operator == "!":
            code += self.emit.emit_not(typ, o.frame)
        return code, typ

    def visit_postfix_expression(self, node: "PostfixExpression", o: Access = None):
        """
        Visit postfix expression (method calls, member access, array access).
        """
        if o is None:
            return "", None
        
        code, typ = self.visit(node.primary, o)
        
        for op in node.postfix_ops:
            # Fix: Create a custom object with code and type attributes since Access doesn't support them
            class AccessWithCode:
                def __init__(self, frame, sym, is_left, is_first, code, type):
                    self.frame = frame
                    self.sym = sym
                    self.is_left = is_left
                    self.is_first = is_first
                    self.code = code
                    self.type = type
            
            o_new = AccessWithCode(o.frame, o.sym, o.is_left, False, code, typ)
            code, typ = self.visit(op, o_new)
            
        return code, typ

    def visit_method_call(self, node: "MethodCall", o: Any = None):
        """
        Visit method call.
        """
        frame = o.frame
        sym_list = o.sym
        code = o.code
        typ = o.type
        
        # Get method symbol
        method_name = node.method_name
        
        # Mapping for common built-in or IO aliases
        io_mapping = {
            "print": "writeStr",
            "printInt": "writeInt",
            "printFloat": "writeFloat",
            "printBool": "writeBool",
            "println": "writeStrLn",
            "int2str": "valueOf",
            "bool2str": "valueOf"
        }
        
        actual_name = io_mapping.get(method_name, method_name)
        
        # Look up in provided symbol list or IO_SYMBOL_LIST
        m_sym = next(filter(lambda x: x.name == actual_name, sym_list), None)
        if m_sym is None:
            from .io import IO_SYMBOL_LIST
            m_sym = next(filter(lambda x: x.name == actual_name, IO_SYMBOL_LIST), None)
            
        # Special case for int2str/bool2str since they use String.valueOf
        if m_sym is None and actual_name == "valueOf":
             if method_name == "int2str":
                 m_sym = Symbol("valueOf", FunctionType([PrimitiveType("int")], PrimitiveType("string")), CName("java/lang/String"))
             elif method_name == "bool2str":
                 m_sym = Symbol("valueOf", FunctionType([PrimitiveType("boolean")], PrimitiveType("string")), CName("java/lang/String"))
        
        # Load arguments
        arg_code = ""
        for arg in node.args:
            ac, at = self.visit(arg, Access(frame, sym_list))
            arg_code += ac
            
        if m_sym and isinstance(m_sym.value, CName):
            # Static call
            code += arg_code
            code += self.emit.emit_invoke_static(f"{m_sym.value.value}/{actual_name}", m_sym.type, frame)
            return code, m_sym.type.return_type
        else:
            # Virtual call
            code += arg_code
            # Assume method is in the type of the receiver (typ)
            class_name = typ.class_name if isinstance(typ, ClassType) else self.current_class
            
            # If we found a symbol but it's not CName, use its type
            m_type = m_sym.type if m_sym else FunctionType([], PrimitiveType("void"))
            
            return code + self.emit.emit_invoke_virtual(f"{class_name}/{actual_name}", m_type, frame), m_type.return_type

    def visit_member_access(self, node: "MemberAccess", o: Any = None):
        """
        Visit member access.
        """
        frame = o.frame
        code = o.code
        typ = o.type
        
        class_name = typ.class_name if isinstance(typ, ClassType) else self.current_class
        field_name = f"{class_name}/{node.member_name}"
        
        if o.is_left:
            # We return the code to write to this field
            # The value to write is already on stack
            # We need to swap if it's an instance field (receiver then value)
            # but wait, visit_postfix_expression doesn't handle this well for fields.
            # Let's assume it's a GET for now and handle assignment separately if needed
            return code + self.emit.emit_put_field(field_name, PrimitiveType("int"), frame), PrimitiveType("int")
        else:
            return code + self.emit.emit_get_field(field_name, PrimitiveType("int"), frame), PrimitiveType("int")

    def visit_array_access(self, node: "ArrayAccess", o: Any = None):
        """
        Visit array access.
        """
        frame = o.frame
        code = o.code
        typ = o.type
        
        idx_code, idx_type = self.visit(node.index, Access(frame, o.sym))
        code += idx_code
        
        elem_type = typ.element_type if isinstance(typ, ArrayType) else PrimitiveType("int")
        
        if o.is_left:
            # The value to store will be pushed after this
            return code, elem_type
        else:
            return code + self.emit.emit_aload(elem_type, frame), elem_type

    def visit_object_creation(self, node: "ObjectCreation", o: Access = None):
        """
        Visit object creation.
        """
        if o is None:
            return "", None
        frame = o.frame
        
        code = self.emit.jvm.emitNEW(node.class_name)
        frame.push()
        code += self.emit.jvm.emitDUP()
        frame.push()
        
        for arg in node.args:
            ac, at = self.visit(arg, o)
            code += ac
            
        code += self.emit.emit_invoke_special(frame, f"{node.class_name}/<init>", FunctionType([], PrimitiveType("void")))
        return code, ClassType(node.class_name)

    def visit_identifier(self, node: "Identifier", o: Access = None):
        """
        Visit identifier - generate code to read variable.
        """
        if o is None:
            return "", None
        
        # Mapping for common built-in or IO aliases
        io_mapping = {
            "print": "writeStr",
            "printInt": "writeInt",
            "printFloat": "writeFloat",
            "printBool": "writeBool",
            "println": "writeStrLn",
            "int2str": "valueOf",
            "bool2str": "valueOf"
        }
        
        target_name = io_mapping.get(node.name, node.name)
        
        # Find symbol
        sym = next(filter(lambda x: x.name == target_name, o.sym), None)
        if sym is None:
            # Fallback for IO functions
            from .io import IO_SYMBOL_LIST
            io_sym = next(filter(lambda x: x.name == target_name, IO_SYMBOL_LIST), None)
            if io_sym:
                return "", io_sym.type
                
            # Special case for int2str/bool2str if not in IO_SYMBOL_LIST
            if target_name == "valueOf":
                if node.name == "int2str":
                    return "", FunctionType([PrimitiveType("int")], PrimitiveType("string"))
                if node.name == "bool2str":
                    return "", FunctionType([PrimitiveType("boolean")], PrimitiveType("string"))

            raise IllegalOperandException(f"Undeclared identifier: {node.name}")
        
        if type(sym.value) is Index:
            code = self.emit.emit_read_var(
                sym.name, sym.type, sym.value.value, o.frame
            )
            return code, sym.type
        elif type(sym.value) is CName:
            # It's a class or static member
            return "", sym.type
        else:
            return "", sym.type

    def visit_this_expression(self, node: "ThisExpression", o: Access = None):
        """
        Visit this expression - load 'this' reference.
        """
        if o is None:
            return "", None
        
        # Find 'this' in symbol table (should be at index 0 for instance methods)
        this_sym = next(filter(lambda x: x.name == "this", o.sym), None)
        if this_sym is None:
            raise IllegalOperandException("'this' not available in static context")
        
        if type(this_sym.value) is Index:
            code = self.emit.emit_read_var(
                "this", this_sym.type, this_sym.value.value, o.frame
            )
            return code, this_sym.type
        else:
            raise IllegalOperandException("Invalid 'this' reference")

    def visit_parenthesized_expression(
        self, node: "ParenthesizedExpression", o: Access = None
    ):
        """
        Visit parenthesized expression - just visit inner expression.
        """
        return self.visit(node.expr, o)

    # ============================================================================
    # Literals
    # ============================================================================

    def visit_int_literal(self, node: "IntLiteral", o: Access = None):
        """
        Visit integer literal - push integer constant.
        """
        if o is None:
            return "", None
        code = self.emit.emit_push_iconst(node.value, o.frame)
        return code, PrimitiveType("int")

    def visit_float_literal(self, node: "FloatLiteral", o: Access = None):
        """
        Visit float literal - push float constant.
        """
        if o is None:
            return "", None
        code = self.emit.emit_push_fconst(str(node.value), o.frame)
        return code, PrimitiveType("float")

    def visit_bool_literal(self, node: "BoolLiteral", o: Access = None):
        """
        Visit boolean literal - push boolean constant.
        """
        if o is None:
            return "", None
        value_str = "1" if node.value else "0"
        code = self.emit.emit_push_iconst(value_str, o.frame)
        return code, PrimitiveType("boolean")

    def visit_string_literal(self, node: "StringLiteral", o: Access = None):
        """
        Visit string literal - push string constant.
        """
        if o is None:
            return "", None
        code = self.emit.emit_push_const('"' + node.value + '"', PrimitiveType("string"), o.frame)
        return code, PrimitiveType("string")

    def visit_array_literal(self, node: "ArrayLiteral", o: Access = None):
        """
        Visit array literal.
        """
        if o is None:
            return "", None
        frame = o.frame
        
        # For simplicity, assume int array
        code = self.emit.emit_push_iconst(len(node.value), frame)
        code += self.emit.jvm.emitNEWARRAY("int")
        # Stack: [array_ref]
        
        for i, expr in enumerate(node.value):
            code += self.emit.jvm.emitDUP()
            frame.push()
            code += self.emit.emit_push_iconst(i, frame)
            ec, et = self.visit(expr, o)
            code += ec
            code += self.emit.emit_astore(PrimitiveType("int"), frame)
            
        return code, ArrayType(PrimitiveType("int"), len(node.value))

    def visit_method_invocation(self, node: "MethodCall", o: Any = None):
        """
        Visit method invocation (PostfixOp).
        """
        return self.visit_method_call(node, o)

    def visit_static_member_access(self, node: "StaticMemberAccess", o: Any = None):
        """
        Visit static member access.
        """
        frame = o.frame
        field_name = f"{node.class_name}/{node.member_name}"
        if o.is_left:
            return self.emit.emit_put_static(field_name, PrimitiveType("int"), frame), PrimitiveType("int")
        else:
            return self.emit.emit_get_static(field_name, PrimitiveType("int"), frame), PrimitiveType("int")

    def visit_static_method_invocation(self, node: "StaticMethodCall", o: Any = None):
        """
        Visit static method invocation.
        """
        frame = o.frame
        # Load arguments
        arg_code = ""
        for arg in node.args:
            ac, at = self.visit(arg, Access(frame, o.sym))
            arg_code += ac
            
        # We need the signature here. For now assume it's void or try to find it.
        # This is a placeholder since we don't have a full symbol table.
        return arg_code + self.emit.emit_invoke_static(f"{node.class_name}/{node.method_name}", FunctionType([], PrimitiveType("void")), frame), PrimitiveType("void")

    def visit_nil_literal(self, node: "NilLiteral", o: Access = None):
        """
        Visit nil literal - push null reference.
        """
        if o is None:
            return "", None
        o.frame.push()
        code = self.emit.jvm.emitPUSHNULL()
        return code, None  # Type will be determined by context


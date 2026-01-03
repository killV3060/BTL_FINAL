"""
Test cases for OPLang code generation.
This file contains test cases for the code generator.
Students should add more test cases here.
"""

from src.utils.nodes import *
from utils import CodeGenerator, ASTGenerator


def test_001():
    """Test basic class with main method and print statement"""
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,  # is_static
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([], [
                        MethodInvocationStatement(
                            PostfixExpression(
                                Identifier("io"),
                                [MethodCall("writeStr", [StringLiteral("Hello World")])]
                            )
                        )
                    ])
                )
            ]
        )
    ])
    expected = "Hello World"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_002():
    """Test integer literal"""
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([], [
                        MethodInvocationStatement(
                            PostfixExpression(
                                Identifier("io"),
                                [MethodCall("writeInt", [IntLiteral(42)])]
                            )
                        )
                    ])
                )
            ]
        )
    ])
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


# TODO: Add more test cases here
# Students should implement at least 100 test cases covering:
# - All literal types (int, float, boolean, string, array, nil)
# - Variable declarations and assignments
# - Binary operations (+, -, *, /, %, ==, !=, <, >, <=, >=, &&, ||)
# - Unary operations (-, +, !)
# - Control flow (if, for, break, continue)
# - Return statements
# - Method calls (static and instance)
# - Member access
# - Array access
# - Object creation
# - This expression
# - Constructors and destructors
# - Inheritance and polymorphism


def test_003():
    """Test float literal"""
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([], [
                        MethodInvocationStatement(
                            PostfixExpression(
                                Identifier("io"),
                                [MethodCall("writeFloat", [FloatLiteral(3.14)])]
                            )
                        )
                    ])
                )
            ]
        )
    ])
    expected = "3.14"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_004():
    """Test boolean literal"""
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([], [
                        MethodInvocationStatement(
                            PostfixExpression(
                                Identifier("io"),
                                [MethodCall("writeBool", [BoolLiteral(True)])]
                            )
                        )
                    ])
                )
            ]
        )
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_005():
    """Test integer variable"""
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([
                        VariableDecl(
                            False,
                            PrimitiveType("int"),
                            [Variable("x", IntLiteral(10))]
                        )], [
                        MethodInvocationStatement(
                            PostfixExpression(
                                Identifier("io"),
                                [MethodCall("writeInt", [Identifier("x")])]
                            )
                        )
                    ])
                )
            ]
        )
    ])
    expected = "10"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_006():
    """Test float variable"""
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([
                        VariableDecl(
                            False,
                            PrimitiveType("float"),
                            [Variable("x", FloatLiteral(3.14))]
                        )], [
                        MethodInvocationStatement(
                            PostfixExpression(
                                Identifier("io"),
                                [MethodCall("writeFloat", [Identifier("x")])]
                            )
                        )
                    ])
                )
            ]
        )
    ])
    expected = "3.14"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_007():
    """Test string variable"""
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([
                        VariableDecl(
                            False,
                            PrimitiveType("string"),
                            [Variable("x", StringLiteral("Hello World"))]
                        )], [
                        MethodInvocationStatement(
                            PostfixExpression(
                                Identifier("io"),
                                [MethodCall("writeStr", [Identifier("x")])]
                            )
                        )
                    ])
                )
            ]
        )
    ])
    expected = "Hello World"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_008():
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([
                        VariableDecl(
                            False,
                            PrimitiveType("int"),
                            [Variable("x", None)]
                        )], [
                        AssignmentStatement(
                            IdLHS("x"), 
                            IntLiteral(10)
                        ),
                        MethodInvocationStatement(
                            PostfixExpression(
                                Identifier("io"),
                                [MethodCall("writeInt", [Identifier("x")])]
                            )
                        )
                    ])
                )
            ]
        )
    ])
    expected = "10"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_009():
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([
                        VariableDecl(
                            False,
                            PrimitiveType("float"),
                            [Variable("x", None)]
                        )], [
                        AssignmentStatement(
                            IdLHS("x"), 
                            FloatLiteral(3.14)
                        ),
                        MethodInvocationStatement(
                            PostfixExpression(
                                Identifier("io"),
                                [MethodCall("writeFloat", [Identifier("x")])]
                            )
                        )
                    ])
                )
            ]
        )
    ])
    expected = "3.14"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_010():
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([
                        VariableDecl(
                            False,
                            PrimitiveType("string"),
                            [Variable("x", None)]
                        )], [
                        AssignmentStatement(
                            IdLHS("x"), 
                            StringLiteral("Hello World")
                        ),
                        MethodInvocationStatement(
                            PostfixExpression(
                                Identifier("io"),
                                [MethodCall("writeStr", [Identifier("x")])]
                            )
                        )
                    ])
                )
            ]
        )
    ])
    expected = "Hello World"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_011():
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([
                        VariableDecl(
                            False,
                            PrimitiveType("int"),
                            [Variable("x", None)]
                        )], [
                        AssignmentStatement(
                            IdLHS("x"), 
                            IntLiteral(10)
                        ),
                        MethodInvocationStatement(
                            PostfixExpression(
                                Identifier("io"),
                                [MethodCall("writeInt", [UnaryOp("-", Identifier("x"))])]
                            )
                        )
                    ])
                )
            ]
        )
    ])
    expected = "-10"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_012():
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([
                        VariableDecl(
                            False,
                            PrimitiveType("float"),
                            [Variable("x", None)]
                        )], [
                        AssignmentStatement(
                            IdLHS("x"), 
                            FloatLiteral(3.14)
                        ),
                        MethodInvocationStatement(
                            PostfixExpression(
                                Identifier("io"),
                                [MethodCall("writeFloat", [UnaryOp("-", Identifier("x"))])]
                            )
                        )
                    ])
                )
            ]
        )
    ])
    expected = "-3.14"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_013():
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([], [
                        MethodInvocationStatement(
                            PostfixExpression(
                                Identifier("io"),
                                [MethodCall("writeBool", [UnaryOp("!", BoolLiteral(True))])]
                            )
                        )
                    ])
                )
            ]
        )
    ])
    expected = "false"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_014():
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([], [
                        MethodInvocationStatement(
                            PostfixExpression(
                                Identifier("io"),
                                [MethodCall("writeInt", [BinaryOp(IntLiteral(5), "+", IntLiteral(5))])]
                            )
                        )
                    ])
                )
            ]
        )
    ])
    expected = "10"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_015():
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([], [
                        MethodInvocationStatement(
                            PostfixExpression(
                                Identifier("io"),
                                [MethodCall("writeInt", [BinaryOp(IntLiteral(5), "-", IntLiteral(5))])]
                            )
                        )
                    ])
                )
            ]
        )
    ])
    expected = "0"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_016():
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([], [
                        MethodInvocationStatement(
                            PostfixExpression(
                                Identifier("io"),
                                [MethodCall("writeInt", [BinaryOp(IntLiteral(5), "*", IntLiteral(5))])]
                            )
                        )
                    ])
                )
            ]
        )
    ])
    expected = "25"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_016():
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([], [
                        MethodInvocationStatement(
                            PostfixExpression(
                                Identifier("io"),
                                [MethodCall("writeInt", [BinaryOp(IntLiteral(10), "+", BinaryOp(IntLiteral(5), "*",IntLiteral(2)))])]
                            )
                        )
                    ])
                )
            ]
        )
    ])
    expected = "20"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_017():
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([], [
                        MethodInvocationStatement(
                            PostfixExpression(
                                Identifier("io"),
                                [MethodCall("writeFloatLn", [BinaryOp(IntLiteral(5), "/", IntLiteral(2))])]
                            )
                        ),
                        MethodInvocationStatement(
                            PostfixExpression(
                                Identifier("io"),
                                [MethodCall("writeInt", [BinaryOp(IntLiteral(5), "\\", IntLiteral(2))])]
                            )
                        )
                    ])
                )
            ]
        )
    ])
    expected = "2.5\n2"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_018():
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([], [
                        MethodInvocationStatement(
                            PostfixExpression(
                                Identifier("io"),
                                [MethodCall("writeStr", [BinaryOp(StringLiteral("TCP"), "^", StringLiteral("/IP"))])]
                            )
                        )
                    ])
                )
            ]
        )
    ])
    expected = "TCP/IP"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_019():
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([], [
                        IfStatement(
                            BoolLiteral(True),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    Identifier("io"),
                                    [MethodCall("writeStr", [StringLiteral("Lau Thai chua cay")])])
                            ),
                            None
                        )
                    ])
                )
            ]
        )
    ])
    expected = "Lau Thai chua cay"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_020():
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([
                        VariableDecl(
                            False,
                            PrimitiveType("int"),
                            [Variable("x", IntLiteral(10))]
                    )], [
                            IfStatement(
                                BinaryOp(Identifier("x"), ">", IntLiteral(5)),
                                IfStatement(
                                    BinaryOp(Identifier("x"), "<", IntLiteral(15)),
                                    MethodInvocationStatement(
                                        PostfixExpression(
                                            Identifier("io"),
                                            [MethodCall("writeInt", [IntLiteral(100)])])
                                    ),
                                    None
                                ),
                                None
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "100"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_021():
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([
                        VariableDecl(
                            False,
                            PrimitiveType("int"),
                            [Variable("i", None)]
                    )], [
                            ForStatement(
                                "i", 
                                IntLiteral(1), 
                                "to", 
                                IntLiteral(5), 
                                MethodInvocationStatement(
                                    PostfixExpression(Identifier("io"), [MethodCall("writeInt", [Identifier("i")])])
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "12345"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_021():
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([
                        VariableDecl(
                            False,
                            PrimitiveType("int"),
                            [Variable("i", None)]
                    )], [
                            ForStatement(
                                "i", 
                                IntLiteral(5), 
                                "downto", 
                                IntLiteral(1), 
                                MethodInvocationStatement(
                                    PostfixExpression(Identifier("io"), [MethodCall("writeInt", [Identifier("i")])])
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "54321"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_022():
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([
                        VariableDecl(
                            False,
                            PrimitiveType("int"),
                            [Variable("i", None)]
                        ), VariableDecl(
                            False,
                            PrimitiveType("int"),
                            [Variable("n", IntLiteral(0))]
                    )], [
                            ForStatement(
                                "i", 
                                IntLiteral(1), 
                                "to", 
                                IntLiteral(9), 
                                AssignmentStatement(IdLHS("n"), BinaryOp(Identifier("n"), "+", Identifier("i")))
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    Identifier("io"), 
                                    [MethodCall("writeInt", [Identifier("n")])]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "45"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_023():
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement(
                        [
                            VariableDecl(
                                False,
                                ArrayType(
                                    PrimitiveType("boolean"),
                                    2
                                ),
                                [
                                    Variable(
                                        "bool",
                                        ArrayLiteral(
                                            [
                                                BoolLiteral(True),
                                                BoolLiteral(False)
                                            ]
                                        )
                                    )
                                ]
                            )
                        ],
                        [
                            MethodInvocationStatement(
                                PostfixExpression(
                                    Identifier("io"),
                                    [
                                        MethodCall(
                                            "writeBool",
                                            [
                                                PostfixExpression(
                                                    Identifier("bool"),
                                                    [ArrayAccess(IntLiteral(0))]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_024():
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    is_static=True,
                    return_type=PrimitiveType("void"),
                    name="main",
                    params=[],
                    body=BlockStatement(
                        var_decls=[
                            VariableDecl(
                                is_final=False,
                                var_type=ArrayType(PrimitiveType("int"), 3),
                                variables=[
                                    Variable(
                                        name="arr",
                                        init_value=ArrayLiteral([
                                            IntLiteral(1),
                                            IntLiteral(2),
                                            IntLiteral(3)
                                        ])
                                    )
                                ]
                            )
                        ],
                        statements=[
                            AssignmentStatement(
                                lhs=PostfixLHS(
                                    postfix_expr=PostfixExpression(
                                        primary=Identifier("arr"),
                                        postfix_ops=[ArrayAccess(index=IntLiteral(1))]
                                    )
                                ),
                                rhs=IntLiteral(10)
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    primary=Identifier("io"),
                                    postfix_ops=[MethodCall("writeIntLn", [
                                        PostfixExpression(Identifier("arr"), [ArrayAccess(IntLiteral(0))])
                                    ])]
                                )
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    primary=Identifier("io"),
                                    postfix_ops=[MethodCall("writeIntLn", [
                                        PostfixExpression(Identifier("arr"), [ArrayAccess(IntLiteral(1))])
                                    ])]
                                )
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    primary=Identifier("io"),
                                    postfix_ops=[MethodCall("writeInt", [
                                        PostfixExpression(Identifier("arr"), [ArrayAccess(IntLiteral(2))])
                                    ])]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "1\n10\n3"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_025():
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    is_static=True,
                    return_type=PrimitiveType("void"),
                    name="main",
                    params=[],
                    body=BlockStatement(
                        var_decls=[
                            VariableDecl(
                                is_final=False,
                                var_type=PrimitiveType("int"),
                                variables=[
                                    Variable("a", IntLiteral(100)),
                                    Variable("b", IntLiteral(1)),
                                    Variable("c", IntLiteral(54))
                                ]
                            ),
                            VariableDecl(
                                is_final=False,
                                var_type=PrimitiveType("int"),
                                variables=[
                                    Variable("max")
                                ]
                            )
                        ],
                        statements=[
                            IfStatement(
                                condition=ParenthesizedExpression(
                                    expr=BinaryOp(
                                        left=Identifier("a"),
                                        operator=">",
                                        right=Identifier("b")
                                    )
                                ),
                                then_stmt=BlockStatement(
                                    var_decls=[],
                                    statements=[
                                        IfStatement(
                                            condition=ParenthesizedExpression(
                                                expr=BinaryOp(
                                                    left=Identifier("a"),
                                                    operator=">",
                                                    right=Identifier("c")
                                                )
                                            ),
                                            then_stmt=BlockStatement(
                                                var_decls=[],
                                                statements=[
                                                    AssignmentStatement(
                                                        lhs=IdLHS("max"),
                                                        rhs=Identifier("a")
                                                    )
                                                ]
                                            ),
                                            else_stmt=BlockStatement(
                                                var_decls=[],
                                                statements=[
                                                    AssignmentStatement(
                                                        lhs=IdLHS("max"),
                                                        rhs=Identifier("c")
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                ),
                                else_stmt=BlockStatement(
                                    var_decls=[],
                                    statements=[
                                        IfStatement(
                                            condition=ParenthesizedExpression(
                                                expr=BinaryOp(
                                                    left=Identifier("b"),
                                                    operator=">",
                                                    right=Identifier("c")
                                                )
                                            ),
                                            then_stmt=BlockStatement(
                                                var_decls=[],
                                                statements=[
                                                    AssignmentStatement(
                                                        lhs=IdLHS("max"),
                                                        rhs=Identifier("b")
                                                    )
                                                ]
                                            ),
                                            else_stmt=BlockStatement(
                                                var_decls=[],
                                                statements=[
                                                    AssignmentStatement(
                                                        lhs=IdLHS("max"),
                                                        rhs=Identifier("c")
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                )
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    primary=Identifier("io"),
                                    postfix_ops=[
                                        MethodCall(
                                            method_name="writeInt",
                                            args=[Identifier("max")]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "100"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_026():
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("int"),
                    "hello",
                    [],
                    BlockStatement(
                        [],
                        [
                            ReturnStatement(
                                IntLiteral(1305)
                            )
                        ]
                    )
                ),
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement(
                        [],
                        [
                            MethodInvocationStatement(
                                PostfixExpression(
                                    Identifier("io"),
                                    [
                                        MethodCall(
                                            "writeInt",
                                            [
                                                PostfixExpression(
                                                    Identifier("Main"),
                                                    [
                                                        MethodCall(
                                                            "hello",
                                                            []
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "1305"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_027():
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("int"),
                    "no_shutdown",
                    [],
                    BlockStatement(
                        [],
                        [
                            ReturnStatement(IntLiteral(36))
                        ]
                    )
                ),
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement(
                        [],
                        [
                            MethodInvocationStatement(
                                PostfixExpression(
                                    Identifier("io"),
                                    [
                                        MethodCall(
                                            "writeInt",
                                            [
                                                PostfixExpression(
                                                    Identifier("Main"),
                                                    [MethodCall("no_shutdown", [])]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "36"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_028():
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement(
                        var_decls=[
                            VariableDecl(
                                False,
                                PrimitiveType("int"),
                                [
                                    Variable(
                                        "a",
                                        IntLiteral(1)
                                    )
                                ]
                            )
                        ],
                        statements=[
                            BlockStatement(
                                var_decls=[
                                    VariableDecl(
                                        False,
                                        PrimitiveType("int"),
                                        [
                                            Variable(
                                                "a",
                                                None
                                            )
                                        ]
                                    )
                                ],
                                statements=[
                                    AssignmentStatement(
                                        IdLHS("a"),
                                        IntLiteral(2)
                                    ),
                                    MethodInvocationStatement(
                                        PostfixExpression(
                                            Identifier("io"),
                                            [
                                                MethodCall(
                                                    "writeInt",
                                                    [Identifier("a")]
                                                )
                                            ]
                                        )
                                    )
                                ]
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    Identifier("io"),
                                    [
                                        MethodCall(
                                            "writeInt",
                                            [Identifier("a")]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "21"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_029():
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "foo",
                    [
                        Parameter(
                            PrimitiveType("int"),
                            "a"
                        )
                    ],
                    BlockStatement(
                        var_decls=[],
                        statements=[
                            MethodInvocationStatement(
                                PostfixExpression(
                                    Identifier("io"),
                                    [
                                        MethodCall(
                                            "writeInt",
                                            [Identifier("a")]
                                        )
                                    ]
                                )
                            ),
                            AssignmentStatement(
                                IdLHS("a"),
                                IntLiteral(1)
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    Identifier("io"),
                                    [
                                        MethodCall(
                                            "writeInt",
                                            [Identifier("a")]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ),
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement(
                        var_decls=[
                            VariableDecl(
                                False,
                                PrimitiveType("int"),
                                [
                                    Variable(
                                        "a",
                                        IntLiteral(2)
                                    )
                                ]
                            )
                        ],
                        statements=[
                            MethodInvocationStatement(
                                PostfixExpression(
                                    Identifier("Main"),
                                    [
                                        MethodCall(
                                            "foo",
                                            [Identifier("a")]
                                        )
                                    ]
                                )
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    Identifier("io"),
                                    [
                                        MethodCall(
                                            "writeInt",
                                            [Identifier("a")]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "212"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_030():
    """Test writing value to an attribute of Main class"""
    ast = Program([
        ClassDecl(
            "Main", 
            None, 
            [
                AttributeDecl(
                    False,
                    False,
                    PrimitiveType("int"), 
                    [Attribute("x", None)]
                ),
                MethodDecl(
                    True,
                    PrimitiveType("void"), 
                    "main", 
                    [], 
                    BlockStatement(
                        [
                            VariableDecl(
                                False, 
                                ClassType("Main"), 
                                [Variable("m", ObjectCreation("Main", []))]
                            )
                        ],
                        [
                            AssignmentStatement(
                                PostfixLHS(
                                    PostfixExpression(
                                        Identifier("m"), 
                                        [MemberAccess("x")]
                                    )
                                ),
                                IntLiteral(10)
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    Identifier("io"),
                                    [
                                        MethodCall(
                                            "writeInt", 
                                            [
                                                PostfixExpression(
                                                    Identifier("m"), 
                                                    [MemberAccess("x")]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "10"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_031():
    """Test writing value to an attribute of Main class"""
    ast = Program([
        ClassDecl(
            "Main", 
            None, 
            [
                AttributeDecl(
                    False,
                    False,
                    PrimitiveType("float"), 
                    [Attribute("x", None)]
                ),
                MethodDecl(
                    True,
                    PrimitiveType("void"), 
                    "main", 
                    [], 
                    BlockStatement(
                        [
                            VariableDecl(
                                False, 
                                ClassType("Main"), 
                                [Variable("m", ObjectCreation("Main", []))]
                            )
                        ],
                        [
                            AssignmentStatement(
                                PostfixLHS(
                                    PostfixExpression(
                                        Identifier("m"), 
                                        [MemberAccess("x")]
                                    )
                                ),
                                FloatLiteral(3.14)
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    Identifier("io"),
                                    [
                                        MethodCall(
                                            "writeFloat", 
                                            [
                                                PostfixExpression(
                                                    Identifier("m"), 
                                                    [MemberAccess("x")]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "3.14"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_032():
    """Test writing value to an attribute of Main class"""
    ast = Program([
        ClassDecl(
            "Main", 
            None, 
            [
                AttributeDecl(
                    False,
                    False,
                    PrimitiveType("string"), 
                    [Attribute("x", None)]
                ),
                MethodDecl(
                    True,
                    PrimitiveType("void"), 
                    "main", 
                    [], 
                    BlockStatement(
                        [
                            VariableDecl(
                                False, 
                                ClassType("Main"), 
                                [Variable("m", ObjectCreation("Main", []))]
                            )
                        ],
                        [
                            AssignmentStatement(
                                PostfixLHS(
                                    PostfixExpression(
                                        Identifier("m"), 
                                        [MemberAccess("x")]
                                    )
                                ),
                                StringLiteral("Banh Dau Xanh")
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    Identifier("io"),
                                    [
                                        MethodCall(
                                            "writeStr", 
                                            [
                                                PostfixExpression(
                                                    Identifier("m"), 
                                                    [MemberAccess("x")]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "Banh Dau Xanh"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_033():
    """Test writing value to an attribute of Main class"""
    ast = Program([
        ClassDecl(
            "Main", 
            None, 
            [
                AttributeDecl(
                    False,
                    False,
                    PrimitiveType("string"), 
                    [Attribute("x", None)]
                ),
                MethodDecl(
                    True,
                    PrimitiveType("void"), 
                    "main", 
                    [], 
                    BlockStatement(
                        [
                            VariableDecl(
                                False, 
                                ClassType("Main"), 
                                [Variable("m", ObjectCreation("Main", []))]
                            )
                        ],
                        [
                            AssignmentStatement(
                                PostfixLHS(
                                    PostfixExpression(
                                        Identifier("m"), 
                                        [MemberAccess("x")]
                                    )
                                ),
                                StringLiteral("Nguyen ly ngon ngu lap trinh")
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    Identifier("io"),
                                    [
                                        MethodCall(
                                            "writeStr", 
                                            [
                                                PostfixExpression(
                                                    Identifier("m"), 
                                                    [MemberAccess("x")]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "Nguyen ly ngon ngu lap trinh"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_034():
    """Test writing value to an attribute of Main class"""
    ast = Program([
        ClassDecl(
            "Main", 
            None, 
            [
                AttributeDecl(
                    False,
                    False,
                    PrimitiveType("string"), 
                    [Attribute("x", None)]
                ),
                MethodDecl(
                    True,
                    PrimitiveType("void"), 
                    "main", 
                    [], 
                    BlockStatement(
                        [
                            VariableDecl(
                                False, 
                                ClassType("Main"), 
                                [Variable("m", ObjectCreation("Main", []))]
                            )
                        ],
                        [
                            AssignmentStatement(
                                PostfixLHS(
                                    PostfixExpression(
                                        Identifier("m"), 
                                        [MemberAccess("x")]
                                    )
                                ),
                                StringLiteral("Mang may tinh")
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    Identifier("io"),
                                    [
                                        MethodCall(
                                            "writeStr", 
                                            [
                                                PostfixExpression(
                                                    Identifier("m"), 
                                                    [MemberAccess("x")]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "Mang may tinh"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_035():
    """Test writing value to an attribute of Main class"""
    ast = Program([
        ClassDecl(
            "Main", 
            None, 
            [
                AttributeDecl(
                    False,
                    False,
                    PrimitiveType("string"), 
                    [Attribute("x", None)]
                ),
                MethodDecl(
                    True,
                    PrimitiveType("void"), 
                    "main", 
                    [], 
                    BlockStatement(
                        [
                            VariableDecl(
                                False, 
                                ClassType("Main"), 
                                [Variable("m", ObjectCreation("Main", []))]
                            )
                        ],
                        [
                            AssignmentStatement(
                                PostfixLHS(
                                    PostfixExpression(
                                        Identifier("m"), 
                                        [MemberAccess("x")]
                                    )
                                ),
                                StringLiteral("Cong nghe phan mem")
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    Identifier("io"),
                                    [
                                        MethodCall(
                                            "writeStr", 
                                            [
                                                PostfixExpression(
                                                    Identifier("m"), 
                                                    [MemberAccess("x")]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "Cong nghe phan mem"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_036():
    """Test writing value to an attribute of Main class"""
    ast = Program([
        ClassDecl(
            "Main", 
            None, 
            [
                AttributeDecl(
                    False,
                    False,
                    PrimitiveType("string"), 
                    [Attribute("x", None)]
                ),
                MethodDecl(
                    True,
                    PrimitiveType("void"), 
                    "main", 
                    [], 
                    BlockStatement(
                        [
                            VariableDecl(
                                False, 
                                ClassType("Main"), 
                                [Variable("m", ObjectCreation("Main", []))]
                            )
                        ],
                        [
                            AssignmentStatement(
                                PostfixLHS(
                                    PostfixExpression(
                                        Identifier("m"), 
                                        [MemberAccess("x")]
                                    )
                                ),
                                StringLiteral("Thanh Hoa")
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    Identifier("io"),
                                    [
                                        MethodCall(
                                            "writeStr", 
                                            [
                                                PostfixExpression(
                                                    Identifier("m"), 
                                                    [MemberAccess("x")]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "Thanh Hoa"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_037():
    """Test writing value to an attribute of Main class"""
    ast = Program([
        ClassDecl(
            "Main", 
            None, 
            [
                AttributeDecl(
                    False,
                    False,
                    PrimitiveType("string"), 
                    [Attribute("x", None)]
                ),
                MethodDecl(
                    True,
                    PrimitiveType("void"), 
                    "main", 
                    [], 
                    BlockStatement(
                        [
                            VariableDecl(
                                False, 
                                ClassType("Main"), 
                                [Variable("m", ObjectCreation("Main", []))]
                            )
                        ],
                        [
                            AssignmentStatement(
                                PostfixLHS(
                                    PostfixExpression(
                                        Identifier("m"), 
                                        [MemberAccess("x")]
                                    )
                                ),
                                StringLiteral("He co so du lieu")
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    Identifier("io"),
                                    [
                                        MethodCall(
                                            "writeStr", 
                                            [
                                                PostfixExpression(
                                                    Identifier("m"), 
                                                    [MemberAccess("x")]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "He co so du lieu"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_038():
    """Test writing value to an attribute of Main class"""
    ast = Program([
        ClassDecl(
            "Main", 
            None, 
            [
                AttributeDecl(
                    False,
                    False,
                    PrimitiveType("string"), 
                    [Attribute("x", None)]
                ),
                MethodDecl(
                    True,
                    PrimitiveType("void"), 
                    "main", 
                    [], 
                    BlockStatement(
                        [
                            VariableDecl(
                                False, 
                                ClassType("Main"), 
                                [Variable("m", ObjectCreation("Main", []))]
                            )
                        ],
                        [
                            AssignmentStatement(
                                PostfixLHS(
                                    PostfixExpression(
                                        Identifier("m"), 
                                        [MemberAccess("x")]
                                    )
                                ),
                                StringLiteral("Do an tong hop")
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    Identifier("io"),
                                    [
                                        MethodCall(
                                            "writeStr", 
                                            [
                                                PostfixExpression(
                                                    Identifier("m"), 
                                                    [MemberAccess("x")]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "Do an tong hop"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_039():
    """Test writing value to an attribute of Main class"""
    ast = Program([
        ClassDecl(
            "Main", 
            None, 
            [
                AttributeDecl(
                    False,
                    False,
                    PrimitiveType("string"), 
                    [Attribute("x", None)]
                ),
                MethodDecl(
                    True,
                    PrimitiveType("void"), 
                    "main", 
                    [], 
                    BlockStatement(
                        [
                            VariableDecl(
                                False, 
                                ClassType("Main"), 
                                [Variable("m", ObjectCreation("Main", []))]
                            )
                        ],
                        [
                            AssignmentStatement(
                                PostfixLHS(
                                    PostfixExpression(
                                        Identifier("m"), 
                                        [MemberAccess("x")]
                                    )
                                ),
                                StringLiteral("Cau truc du lieu va giai thuat")
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    Identifier("io"),
                                    [
                                        MethodCall(
                                            "writeStr", 
                                            [
                                                PostfixExpression(
                                                    Identifier("m"), 
                                                    [MemberAccess("x")]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "Cau truc du lieu va giai thuat"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_040():
    """Test writing value to an attribute of Main class"""
    ast = Program([
        ClassDecl(
            "Main", 
            None, 
            [
                AttributeDecl(
                    False,
                    False,
                    PrimitiveType("string"), 
                    [Attribute("x", None)]
                ),
                MethodDecl(
                    True,
                    PrimitiveType("void"), 
                    "main", 
                    [], 
                    BlockStatement(
                        [
                            VariableDecl(
                                False, 
                                ClassType("Main"), 
                                [Variable("m", ObjectCreation("Main", []))]
                            )
                        ],
                        [
                            AssignmentStatement(
                                PostfixLHS(
                                    PostfixExpression(
                                        Identifier("m"), 
                                        [MemberAccess("x")]
                                    )
                                ),
                                StringLiteral("Truong Dai hoc Bach khoa TPHCM")
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    Identifier("io"),
                                    [
                                        MethodCall(
                                            "writeStr", 
                                            [
                                                PostfixExpression(
                                                    Identifier("m"), 
                                                    [MemberAccess("x")]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "Truong Dai hoc Bach khoa TPHCM"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_041():
    ast = Program([
        ClassDecl(
            name="Main",
            superclass=None,
            members=[
                AttributeDecl(
                    is_static=False,
                    is_final=False,
                    attr_type=PrimitiveType("int"),
                    attributes=[Attribute("a")]
                ),
                ConstructorDecl(
                    name="Main",
                    params=[Parameter(PrimitiveType("int"), "a")],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            AssignmentStatement(
                                lhs=PostfixLHS(
                                    PostfixExpression(
                                        primary=ThisExpression(),
                                        postfix_ops=[MemberAccess("a")]
                                    )
                                ),
                                rhs=Identifier("a")
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=False,
                    return_type=PrimitiveType("int"),
                    name="test",
                    params=[],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            ReturnStatement(
                                PostfixExpression(
                                    primary=ThisExpression(),
                                    postfix_ops=[MemberAccess("a")]
                                )
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=True,
                    return_type=PrimitiveType("void"),
                    name="main",
                    params=[],
                    body=BlockStatement(
                        var_decls=[
                            VariableDecl(
                                is_final=False,
                                var_type=ClassType("Main"),
                                variables=[
                                    Variable(
                                        name="a",
                                        init_value=ObjectCreation(
                                            class_name="Main",
                                            args=[IntLiteral(5)]
                                        )
                                    )
                                ]
                            )
                        ],
                        statements=[
                            MethodInvocationStatement(
                                method_call=PostfixExpression(
                                    primary=Identifier("io"),
                                    postfix_ops=[
                                        MethodCall(
                                            method_name="writeInt",
                                            args=[
                                                PostfixExpression(
                                                    primary=Identifier("a"),
                                                    postfix_ops=[MethodCall("test", [])]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_042():
    ast = Program([
        ClassDecl(
            name="Main",
            superclass=None,
            members=[
                AttributeDecl(
                    is_static=False,
                    is_final=False,
                    attr_type=PrimitiveType("int"),
                    attributes=[Attribute("a")]
                ),
                ConstructorDecl(
                    name="Main",
                    params=[Parameter(PrimitiveType("int"), "a")],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            AssignmentStatement(
                                lhs=PostfixLHS(
                                    PostfixExpression(
                                        primary=ThisExpression(),
                                        postfix_ops=[MemberAccess("a")]
                                    )
                                ),
                                rhs=Identifier("a")
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=False,
                    return_type=PrimitiveType("int"),
                    name="test",
                    params=[],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            ReturnStatement(
                                PostfixExpression(
                                    primary=ThisExpression(),
                                    postfix_ops=[MemberAccess("a")]
                                )
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=True,
                    return_type=PrimitiveType("void"),
                    name="main",
                    params=[],
                    body=BlockStatement(
                        var_decls=[
                            VariableDecl(
                                is_final=False,
                                var_type=ClassType("Main"),
                                variables=[
                                    Variable(
                                        name="a",
                                        init_value=ObjectCreation(
                                            class_name="Main",
                                            args=[IntLiteral(1)]
                                        )
                                    )
                                ]
                            )
                        ],
                        statements=[
                            MethodInvocationStatement(
                                method_call=PostfixExpression(
                                    primary=Identifier("io"),
                                    postfix_ops=[
                                        MethodCall(
                                            method_name="writeInt",
                                            args=[
                                                PostfixExpression(
                                                    primary=Identifier("a"),
                                                    postfix_ops=[MethodCall("test", [])]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "1"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_043():
    ast = Program([
        ClassDecl(
            name="Main",
            superclass=None,
            members=[
                AttributeDecl(
                    is_static=False,
                    is_final=False,
                    attr_type=PrimitiveType("int"),
                    attributes=[Attribute("a")]
                ),
                ConstructorDecl(
                    name="Main",
                    params=[Parameter(PrimitiveType("int"), "a")],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            AssignmentStatement(
                                lhs=PostfixLHS(
                                    PostfixExpression(
                                        primary=ThisExpression(),
                                        postfix_ops=[MemberAccess("a")]
                                    )
                                ),
                                rhs=Identifier("a")
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=False,
                    return_type=PrimitiveType("int"),
                    name="test",
                    params=[],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            ReturnStatement(
                                PostfixExpression(
                                    primary=ThisExpression(),
                                    postfix_ops=[MemberAccess("a")]
                                )
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=True,
                    return_type=PrimitiveType("void"),
                    name="main",
                    params=[],
                    body=BlockStatement(
                        var_decls=[
                            VariableDecl(
                                is_final=False,
                                var_type=ClassType("Main"),
                                variables=[
                                    Variable(
                                        name="a",
                                        init_value=ObjectCreation(
                                            class_name="Main",
                                            args=[IntLiteral(2)]
                                        )
                                    )
                                ]
                            )
                        ],
                        statements=[
                            MethodInvocationStatement(
                                method_call=PostfixExpression(
                                    primary=Identifier("io"),
                                    postfix_ops=[
                                        MethodCall(
                                            method_name="writeInt",
                                            args=[
                                                PostfixExpression(
                                                    primary=Identifier("a"),
                                                    postfix_ops=[MethodCall("test", [])]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "2"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_044():
    ast = Program([
        ClassDecl(
            name="Main",
            superclass=None,
            members=[
                AttributeDecl(
                    is_static=False,
                    is_final=False,
                    attr_type=PrimitiveType("int"),
                    attributes=[Attribute("a")]
                ),
                ConstructorDecl(
                    name="Main",
                    params=[Parameter(PrimitiveType("int"), "a")],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            AssignmentStatement(
                                lhs=PostfixLHS(
                                    PostfixExpression(
                                        primary=ThisExpression(),
                                        postfix_ops=[MemberAccess("a")]
                                    )
                                ),
                                rhs=Identifier("a")
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=False,
                    return_type=PrimitiveType("int"),
                    name="test",
                    params=[],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            ReturnStatement(
                                PostfixExpression(
                                    primary=ThisExpression(),
                                    postfix_ops=[MemberAccess("a")]
                                )
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=True,
                    return_type=PrimitiveType("void"),
                    name="main",
                    params=[],
                    body=BlockStatement(
                        var_decls=[
                            VariableDecl(
                                is_final=False,
                                var_type=ClassType("Main"),
                                variables=[
                                    Variable(
                                        name="a",
                                        init_value=ObjectCreation(
                                            class_name="Main",
                                            args=[IntLiteral(3)]
                                        )
                                    )
                                ]
                            )
                        ],
                        statements=[
                            MethodInvocationStatement(
                                method_call=PostfixExpression(
                                    primary=Identifier("io"),
                                    postfix_ops=[
                                        MethodCall(
                                            method_name="writeInt",
                                            args=[
                                                PostfixExpression(
                                                    primary=Identifier("a"),
                                                    postfix_ops=[MethodCall("test", [])]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "3"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_045():
    ast = Program([
        ClassDecl(
            name="Main",
            superclass=None,
            members=[
                AttributeDecl(
                    is_static=False,
                    is_final=False,
                    attr_type=PrimitiveType("int"),
                    attributes=[Attribute("a")]
                ),
                ConstructorDecl(
                    name="Main",
                    params=[Parameter(PrimitiveType("int"), "a")],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            AssignmentStatement(
                                lhs=PostfixLHS(
                                    PostfixExpression(
                                        primary=ThisExpression(),
                                        postfix_ops=[MemberAccess("a")]
                                    )
                                ),
                                rhs=Identifier("a")
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=False,
                    return_type=PrimitiveType("int"),
                    name="test",
                    params=[],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            ReturnStatement(
                                PostfixExpression(
                                    primary=ThisExpression(),
                                    postfix_ops=[MemberAccess("a")]
                                )
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=True,
                    return_type=PrimitiveType("void"),
                    name="main",
                    params=[],
                    body=BlockStatement(
                        var_decls=[
                            VariableDecl(
                                is_final=False,
                                var_type=ClassType("Main"),
                                variables=[
                                    Variable(
                                        name="a",
                                        init_value=ObjectCreation(
                                            class_name="Main",
                                            args=[IntLiteral(4)]
                                        )
                                    )
                                ]
                            )
                        ],
                        statements=[
                            MethodInvocationStatement(
                                method_call=PostfixExpression(
                                    primary=Identifier("io"),
                                    postfix_ops=[
                                        MethodCall(
                                            method_name="writeInt",
                                            args=[
                                                PostfixExpression(
                                                    primary=Identifier("a"),
                                                    postfix_ops=[MethodCall("test", [])]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "4"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_046():
    ast = Program([
        ClassDecl(
            name="Main",
            superclass=None,
            members=[
                AttributeDecl(
                    is_static=False,
                    is_final=False,
                    attr_type=PrimitiveType("int"),
                    attributes=[Attribute("a")]
                ),
                ConstructorDecl(
                    name="Main",
                    params=[Parameter(PrimitiveType("int"), "a")],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            AssignmentStatement(
                                lhs=PostfixLHS(
                                    PostfixExpression(
                                        primary=ThisExpression(),
                                        postfix_ops=[MemberAccess("a")]
                                    )
                                ),
                                rhs=Identifier("a")
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=False,
                    return_type=PrimitiveType("int"),
                    name="test",
                    params=[],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            ReturnStatement(
                                PostfixExpression(
                                    primary=ThisExpression(),
                                    postfix_ops=[MemberAccess("a")]
                                )
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=True,
                    return_type=PrimitiveType("void"),
                    name="main",
                    params=[],
                    body=BlockStatement(
                        var_decls=[
                            VariableDecl(
                                is_final=False,
                                var_type=ClassType("Main"),
                                variables=[
                                    Variable(
                                        name="a",
                                        init_value=ObjectCreation(
                                            class_name="Main",
                                            args=[IntLiteral(5)]
                                        )
                                    )
                                ]
                            )
                        ],
                        statements=[
                            MethodInvocationStatement(
                                method_call=PostfixExpression(
                                    primary=Identifier("io"),
                                    postfix_ops=[
                                        MethodCall(
                                            method_name="writeInt",
                                            args=[
                                                PostfixExpression(
                                                    primary=Identifier("a"),
                                                    postfix_ops=[MethodCall("test", [])]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_047():
    ast = Program([
        ClassDecl(
            name="Main",
            superclass=None,
            members=[
                AttributeDecl(
                    is_static=False,
                    is_final=False,
                    attr_type=PrimitiveType("int"),
                    attributes=[Attribute("a")]
                ),
                ConstructorDecl(
                    name="Main",
                    params=[Parameter(PrimitiveType("int"), "a")],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            AssignmentStatement(
                                lhs=PostfixLHS(
                                    PostfixExpression(
                                        primary=ThisExpression(),
                                        postfix_ops=[MemberAccess("a")]
                                    )
                                ),
                                rhs=Identifier("a")
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=False,
                    return_type=PrimitiveType("int"),
                    name="test",
                    params=[],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            ReturnStatement(
                                PostfixExpression(
                                    primary=ThisExpression(),
                                    postfix_ops=[MemberAccess("a")]
                                )
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=True,
                    return_type=PrimitiveType("void"),
                    name="main",
                    params=[],
                    body=BlockStatement(
                        var_decls=[
                            VariableDecl(
                                is_final=False,
                                var_type=ClassType("Main"),
                                variables=[
                                    Variable(
                                        name="a",
                                        init_value=ObjectCreation(
                                            class_name="Main",
                                            args=[IntLiteral(6)]
                                        )
                                    )
                                ]
                            )
                        ],
                        statements=[
                            MethodInvocationStatement(
                                method_call=PostfixExpression(
                                    primary=Identifier("io"),
                                    postfix_ops=[
                                        MethodCall(
                                            method_name="writeInt",
                                            args=[
                                                PostfixExpression(
                                                    primary=Identifier("a"),
                                                    postfix_ops=[MethodCall("test", [])]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "6"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_048():
    ast = Program([
        ClassDecl(
            name="Main",
            superclass=None,
            members=[
                AttributeDecl(
                    is_static=False,
                    is_final=False,
                    attr_type=PrimitiveType("int"),
                    attributes=[Attribute("a")]
                ),
                ConstructorDecl(
                    name="Main",
                    params=[Parameter(PrimitiveType("int"), "a")],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            AssignmentStatement(
                                lhs=PostfixLHS(
                                    PostfixExpression(
                                        primary=ThisExpression(),
                                        postfix_ops=[MemberAccess("a")]
                                    )
                                ),
                                rhs=Identifier("a")
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=False,
                    return_type=PrimitiveType("int"),
                    name="test",
                    params=[],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            ReturnStatement(
                                PostfixExpression(
                                    primary=ThisExpression(),
                                    postfix_ops=[MemberAccess("a")]
                                )
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=True,
                    return_type=PrimitiveType("void"),
                    name="main",
                    params=[],
                    body=BlockStatement(
                        var_decls=[
                            VariableDecl(
                                is_final=False,
                                var_type=ClassType("Main"),
                                variables=[
                                    Variable(
                                        name="a",
                                        init_value=ObjectCreation(
                                            class_name="Main",
                                            args=[IntLiteral(7)]
                                        )
                                    )
                                ]
                            )
                        ],
                        statements=[
                            MethodInvocationStatement(
                                method_call=PostfixExpression(
                                    primary=Identifier("io"),
                                    postfix_ops=[
                                        MethodCall(
                                            method_name="writeInt",
                                            args=[
                                                PostfixExpression(
                                                    primary=Identifier("a"),
                                                    postfix_ops=[MethodCall("test", [])]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "7"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_049():
    ast = Program([
        ClassDecl(
            name="Main",
            superclass=None,
            members=[
                AttributeDecl(
                    is_static=False,
                    is_final=False,
                    attr_type=PrimitiveType("int"),
                    attributes=[Attribute("a")]
                ),
                ConstructorDecl(
                    name="Main",
                    params=[Parameter(PrimitiveType("int"), "a")],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            AssignmentStatement(
                                lhs=PostfixLHS(
                                    PostfixExpression(
                                        primary=ThisExpression(),
                                        postfix_ops=[MemberAccess("a")]
                                    )
                                ),
                                rhs=Identifier("a")
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=False,
                    return_type=PrimitiveType("int"),
                    name="test",
                    params=[],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            ReturnStatement(
                                PostfixExpression(
                                    primary=ThisExpression(),
                                    postfix_ops=[MemberAccess("a")]
                                )
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=True,
                    return_type=PrimitiveType("void"),
                    name="main",
                    params=[],
                    body=BlockStatement(
                        var_decls=[
                            VariableDecl(
                                is_final=False,
                                var_type=ClassType("Main"),
                                variables=[
                                    Variable(
                                        name="a",
                                        init_value=ObjectCreation(
                                            class_name="Main",
                                            args=[IntLiteral(8)]
                                        )
                                    )
                                ]
                            )
                        ],
                        statements=[
                            MethodInvocationStatement(
                                method_call=PostfixExpression(
                                    primary=Identifier("io"),
                                    postfix_ops=[
                                        MethodCall(
                                            method_name="writeInt",
                                            args=[
                                                PostfixExpression(
                                                    primary=Identifier("a"),
                                                    postfix_ops=[MethodCall("test", [])]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "8"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_050():
    ast = Program([
        ClassDecl(
            name="Main",
            superclass=None,
            members=[
                AttributeDecl(
                    is_static=False,
                    is_final=False,
                    attr_type=PrimitiveType("int"),
                    attributes=[Attribute("a")]
                ),
                ConstructorDecl(
                    name="Main",
                    params=[Parameter(PrimitiveType("int"), "a")],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            AssignmentStatement(
                                lhs=PostfixLHS(
                                    PostfixExpression(
                                        primary=ThisExpression(),
                                        postfix_ops=[MemberAccess("a")]
                                    )
                                ),
                                rhs=Identifier("a")
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=False,
                    return_type=PrimitiveType("int"),
                    name="test",
                    params=[],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            ReturnStatement(
                                PostfixExpression(
                                    primary=ThisExpression(),
                                    postfix_ops=[MemberAccess("a")]
                                )
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=True,
                    return_type=PrimitiveType("void"),
                    name="main",
                    params=[],
                    body=BlockStatement(
                        var_decls=[
                            VariableDecl(
                                is_final=False,
                                var_type=ClassType("Main"),
                                variables=[
                                    Variable(
                                        name="a",
                                        init_value=ObjectCreation(
                                            class_name="Main",
                                            args=[IntLiteral(9)]
                                        )
                                    )
                                ]
                            )
                        ],
                        statements=[
                            MethodInvocationStatement(
                                method_call=PostfixExpression(
                                    primary=Identifier("io"),
                                    postfix_ops=[
                                        MethodCall(
                                            method_name="writeInt",
                                            args=[
                                                PostfixExpression(
                                                    primary=Identifier("a"),
                                                    postfix_ops=[MethodCall("test", [])]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "9"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_051():
    ast = Program([
        ClassDecl(
            name="Main",
            superclass=None,
            members=[
                AttributeDecl(
                    is_static=False,
                    is_final=False,
                    attr_type=PrimitiveType("int"),
                    attributes=[Attribute("a")]
                ),
                ConstructorDecl(
                    name="Main",
                    params=[Parameter(PrimitiveType("int"), "a")],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            AssignmentStatement(
                                lhs=PostfixLHS(
                                    PostfixExpression(
                                        primary=ThisExpression(),
                                        postfix_ops=[MemberAccess("a")]
                                    )
                                ),
                                rhs=Identifier("a")
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=False,
                    return_type=PrimitiveType("int"),
                    name="test",
                    params=[],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            ReturnStatement(
                                PostfixExpression(
                                    primary=ThisExpression(),
                                    postfix_ops=[MemberAccess("a")]
                                )
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=True,
                    return_type=PrimitiveType("void"),
                    name="main",
                    params=[],
                    body=BlockStatement(
                        var_decls=[
                            VariableDecl(
                                is_final=False,
                                var_type=ClassType("Main"),
                                variables=[
                                    Variable(
                                        name="a",
                                        init_value=ObjectCreation(
                                            class_name="Main",
                                            args=[IntLiteral(10)]
                                        )
                                    )
                                ]
                            )
                        ],
                        statements=[
                            MethodInvocationStatement(
                                method_call=PostfixExpression(
                                    primary=Identifier("io"),
                                    postfix_ops=[
                                        MethodCall(
                                            method_name="writeInt",
                                            args=[
                                                PostfixExpression(
                                                    primary=Identifier("a"),
                                                    postfix_ops=[MethodCall("test", [])]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "10"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_052():
    ast = Program([
        ClassDecl(
            name="Main",
            superclass=None,
            members=[
                AttributeDecl(
                    is_static=False,
                    is_final=False,
                    attr_type=PrimitiveType("int"),
                    attributes=[Attribute("a")]
                ),
                ConstructorDecl(
                    name="Main",
                    params=[Parameter(PrimitiveType("int"), "a")],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            AssignmentStatement(
                                lhs=PostfixLHS(
                                    PostfixExpression(
                                        primary=ThisExpression(),
                                        postfix_ops=[MemberAccess("a")]
                                    )
                                ),
                                rhs=Identifier("a")
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=False,
                    return_type=PrimitiveType("int"),
                    name="test",
                    params=[],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            ReturnStatement(
                                PostfixExpression(
                                    primary=ThisExpression(),
                                    postfix_ops=[MemberAccess("a")]
                                )
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=True,
                    return_type=PrimitiveType("void"),
                    name="main",
                    params=[],
                    body=BlockStatement(
                        var_decls=[
                            VariableDecl(
                                is_final=False,
                                var_type=ClassType("Main"),
                                variables=[
                                    Variable(
                                        name="a",
                                        init_value=ObjectCreation(
                                            class_name="Main",
                                            args=[IntLiteral(11)]
                                        )
                                    )
                                ]
                            )
                        ],
                        statements=[
                            MethodInvocationStatement(
                                method_call=PostfixExpression(
                                    primary=Identifier("io"),
                                    postfix_ops=[
                                        MethodCall(
                                            method_name="writeInt",
                                            args=[
                                                PostfixExpression(
                                                    primary=Identifier("a"),
                                                    postfix_ops=[MethodCall("test", [])]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "11"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_053():
    ast = Program([
        ClassDecl(
            name="Main",
            superclass=None,
            members=[
                AttributeDecl(
                    is_static=False,
                    is_final=False,
                    attr_type=PrimitiveType("int"),
                    attributes=[Attribute("a")]
                ),
                ConstructorDecl(
                    name="Main",
                    params=[Parameter(PrimitiveType("int"), "a")],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            AssignmentStatement(
                                lhs=PostfixLHS(
                                    PostfixExpression(
                                        primary=ThisExpression(),
                                        postfix_ops=[MemberAccess("a")]
                                    )
                                ),
                                rhs=Identifier("a")
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=False,
                    return_type=PrimitiveType("int"),
                    name="test",
                    params=[],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            ReturnStatement(
                                PostfixExpression(
                                    primary=ThisExpression(),
                                    postfix_ops=[MemberAccess("a")]
                                )
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=True,
                    return_type=PrimitiveType("void"),
                    name="main",
                    params=[],
                    body=BlockStatement(
                        var_decls=[
                            VariableDecl(
                                is_final=False,
                                var_type=ClassType("Main"),
                                variables=[
                                    Variable(
                                        name="a",
                                        init_value=ObjectCreation(
                                            class_name="Main",
                                            args=[IntLiteral(12)]
                                        )
                                    )
                                ]
                            )
                        ],
                        statements=[
                            MethodInvocationStatement(
                                method_call=PostfixExpression(
                                    primary=Identifier("io"),
                                    postfix_ops=[
                                        MethodCall(
                                            method_name="writeInt",
                                            args=[
                                                PostfixExpression(
                                                    primary=Identifier("a"),
                                                    postfix_ops=[MethodCall("test", [])]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "12"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_054():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [BinaryOp(IntLiteral(10), "+", IntLiteral(20))])
                ]))
            ]))
        ])
    ])
    expected = "30"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_055():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeFloat", [BinaryOp(IntLiteral(10), "+", FloatLiteral(20.5))])
                ]))
            ]))
        ])
    ])
    expected = "30.5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_056():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [BinaryOp(IntLiteral(50), "-", IntLiteral(15))])
                ]))
            ]))
        ])
    ])
    expected = "35"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_057():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeFloat", [BinaryOp(FloatLiteral(10.5), "-", IntLiteral(5))])
                ]))
            ]))
        ])
    ])
    expected = "5.5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_058():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [BinaryOp(IntLiteral(5), "*", IntLiteral(6))])
                ]))
            ]))
        ])
    ])
    expected = "30"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_059():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeFloat", [BinaryOp(FloatLiteral(2.5), "*", FloatLiteral(3.0))])
                ]))
            ]))
        ])
    ])
    expected = "7.5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_060():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeFloat", [BinaryOp(IntLiteral(7), "/", IntLiteral(2))])
                ]))
            ]))
        ])
    ])
    expected = "3.5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_061():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [BinaryOp(IntLiteral(7), "\\", IntLiteral(2))])
                ]))
            ]))
        ])
    ])
    expected = "3"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_062():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [BinaryOp(IntLiteral(7), "%", IntLiteral(2))])
                ]))
            ]))
        ])
    ])
    expected = "1"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_063():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeStr", [BinaryOp(StringLiteral("Hello "), "^", StringLiteral("World"))])
                ]))
            ]))
        ])
    ])
    expected = "Hello World"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_064():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeStr", [BinaryOp(StringLiteral("OP"), "^", StringLiteral("Lang"))])
                ]))
            ]))
        ])
    ])
    expected = "OPLang"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_065():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [BinaryOp(IntLiteral(10), ">", IntLiteral(5))])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_066():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [BinaryOp(IntLiteral(10), "<", FloatLiteral(20.5))])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_067():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [BinaryOp(FloatLiteral(5.5), ">=", FloatLiteral(5.5))])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_068():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [BinaryOp(IntLiteral(10), "<=", IntLiteral(9))])
                ]))
            ]))
        ])
    ])
    expected = "false"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_069():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [BinaryOp(IntLiteral(10), "==", IntLiteral(10))])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_070():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [BinaryOp(FloatLiteral(10.0), "==", IntLiteral(10))])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_071():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [BinaryOp(IntLiteral(5), "!=", IntLiteral(6))])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_072():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [BinaryOp(BoolLiteral(True), "==", BoolLiteral(False))])
                ]))
            ]))
        ])
    ])
    expected = "false"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_073():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [BinaryOp(BoolLiteral(True), "!=", BoolLiteral(False))])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_074():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [BinaryOp(BoolLiteral(True), "&&", BoolLiteral(False))])
                ]))
            ]))
        ])
    ])
    expected = "false"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_075():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [
                        BinaryOp(
                            BoolLiteral(False),
                            "&&",
                            BinaryOp(BinaryOp(IntLiteral(1), "\\", IntLiteral(0)), "==", IntLiteral(0))
                        )
                    ])
                ]))
            ]))
        ])
    ])
    expected = "false"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_076():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [
                        BinaryOp(
                            BoolLiteral(True),
                            "&&",
                            BinaryOp(BinaryOp(IntLiteral(1), "\\", IntLiteral(1)), "==", IntLiteral(0))
                        )
                    ])
                ]))
            ]))
        ])
    ])
    expected = "false"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_077():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [
                        BinaryOp(
                            BoolLiteral(True),
                            "&&",
                            BinaryOp(BinaryOp(IntLiteral(1), "\\", IntLiteral(1)), ">=", IntLiteral(0))
                        )
                    ])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_078():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [
                        BinaryOp(
                            BoolLiteral(True),
                            "&&",
                            BinaryOp(BinaryOp(IntLiteral(1), "\\", IntLiteral(2)), "==", IntLiteral(0))
                        )
                    ])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_079():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [
                        BinaryOp(
                            BoolLiteral(True),
                            "||",
                            BinaryOp(BinaryOp(IntLiteral(1), "\\", IntLiteral(0)), "==", IntLiteral(0))
                        )
                    ])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_080():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [
                        BinaryOp(
                            BoolLiteral(False),
                            "||",
                            BinaryOp(BinaryOp(IntLiteral(1), "\\", IntLiteral(1)), "==", IntLiteral(1))
                        )
                    ])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_081():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, PrimitiveType("int"), [Variable("i", None)])], 
                [
                    ForStatement("i", IntLiteral(1), "to", IntLiteral(3), BlockStatement([], [
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeInt", [Identifier("i")])
                        ]))
                    ]))
                ]
            ))
        ])
    ])
    expected = "123"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_082():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, PrimitiveType("int"), [Variable("i", None)])], 
                [
                    ForStatement("i", IntLiteral(3), "downto", IntLiteral(1), BlockStatement([], [
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeInt", [Identifier("i")])
                        ]))
                    ]))
                ]
            ))
        ])
    ])
    expected = "321"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_083():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, PrimitiveType("int"), [Variable("i", None)])], 
                [
                    ForStatement("i", IntLiteral(1), "to", IntLiteral(5), BlockStatement([], [
                        IfStatement(
                            BinaryOp(Identifier("i"), "==", IntLiteral(3)),
                            BreakStatement(),
                            None
                        ),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeInt", [Identifier("i")])
                        ]))
                    ]))
                ]
            ))
        ])
    ])
    expected = "12"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_084():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, PrimitiveType("int"), [Variable("i", None)])], 
                [
                    ForStatement("i", IntLiteral(1), "to", IntLiteral(5), BlockStatement([], [
                        IfStatement(
                            BinaryOp(Identifier("i"), "==", IntLiteral(3)),
                            ContinueStatement(),
                            None
                        ),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeInt", [Identifier("i")])
                        ]))
                    ]))
                ]
            ))
        ])
    ])
    expected = "1245"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_085():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("int"), "foo", [], BlockStatement(
                [VariableDecl(False, PrimitiveType("int"), [Variable("i", None)])], 
                [
                    ForStatement("i", IntLiteral(1), "to", IntLiteral(5), BlockStatement([], [
                        IfStatement(
                            BinaryOp(Identifier("i"), "==", IntLiteral(3)),
                            ReturnStatement(Identifier("i")), 
                            None
                        )
                    ])),
                    ReturnStatement(IntLiteral(0))
                ]
            )),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        PostfixExpression(Identifier("Main"), [MethodCall("foo", [])])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "3"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_086():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("i", None)]),
                    VariableDecl(False, PrimitiveType("int"), [Variable("j", None)])
                ], 
                [
                    ForStatement("i", IntLiteral(1), "to", IntLiteral(2), BlockStatement([], [
                        ForStatement("j", IntLiteral(1), "to", IntLiteral(2), BlockStatement([], [
                            MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                                MethodCall("writeInt", [Identifier("i")])
                            ])),
                            MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                                MethodCall("writeInt", [Identifier("j")])
                            ]))
                        ]))
                    ]))
                ]
            ))
        ])
    ])
    expected = "11122122"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_087():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("i", None)]),
                    VariableDecl(False, PrimitiveType("int"), [Variable("start", IntLiteral(1))]),
                    VariableDecl(False, PrimitiveType("int"), [Variable("end", IntLiteral(4))])
                ], 
                [
                    ForStatement("i", 
                        BinaryOp(Identifier("start"), "+", IntLiteral(1)), # 2
                        "to", 
                        BinaryOp(Identifier("end"), "-", IntLiteral(1)),   # 3
                        BlockStatement([], [
                            MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                                MethodCall("writeInt", [Identifier("i")])
                            ]))
                        ])
                    )
                ]
            ))
        ])
    ])
    expected = "23"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_088():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                IfStatement(
                    BoolLiteral(True),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeInt", [IntLiteral(1)])])),
                    None
                )
            ]))
        ])
    ])
    expected = "1"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_089():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                IfStatement(
                    BoolLiteral(False),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeInt", [IntLiteral(1)])])),
                    None
                )
            ]))
        ])
    ])
    expected = ""
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_090():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                IfStatement(
                    BoolLiteral(True),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeInt", [IntLiteral(1)])])),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeInt", [IntLiteral(0)])]))
                )
            ]))
        ])
    ])
    expected = "1"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_091():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                IfStatement(
                    BoolLiteral(False),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeInt", [IntLiteral(1)])])),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeInt", [IntLiteral(0)])]))
                )
            ]))
        ])
    ])
    expected = "0"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_092():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                IfStatement(
                    BoolLiteral(True),
                    BlockStatement([], [
                        IfStatement(
                            BoolLiteral(False),
                            MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeInt", [IntLiteral(1)])])),
                            MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeInt", [IntLiteral(2)])]))
                        )
                    ]),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeInt", [IntLiteral(3)])]))
                )
            ]))
        ])
    ])
    expected = "2"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_093():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, PrimitiveType("int"), [Variable("a", IntLiteral(5))])], 
                [
                    IfStatement(
                        BinaryOp(
                            BinaryOp(Identifier("a"), ">", IntLiteral(3)),
                            "&&",
                            BinaryOp(Identifier("a"), "<", IntLiteral(10))
                        ),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeInt", [IntLiteral(1)])])),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeInt", [IntLiteral(0)])]))
                    )
                ]
            ))
        ])
    ])
    expected = "1"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_094():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, PrimitiveType("int"), [Variable("a", IntLiteral(1))])], 
                [
                    IfStatement(
                        BoolLiteral(True),
                        AssignmentStatement(IdLHS("a"), IntLiteral(2)),
                        AssignmentStatement(IdLHS("a"), IntLiteral(3))
                    ),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeInt", [Identifier("a")])]))
                ]
            ))
        ])
    ])
    expected = "2"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_095():
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    is_static=True,
                    return_type=PrimitiveType("void"),
                    name="foo",
                    params=[
                        Parameter(
                            param_type=ArrayType(
                                element_type=PrimitiveType("int"),
                                size=2
                            ),
                            name="a"
                        )
                    ],
                    body=BlockStatement(
                        var_decls=[],
                        statements=[
                            AssignmentStatement(
                                lhs=PostfixLHS(
                                    PostfixExpression(
                                        primary=Identifier("a"),
                                        postfix_ops=[
                                            ArrayAccess(index=IntLiteral(1))
                                        ]
                                    )
                                ),
                                rhs=IntLiteral(2)
                            )
                        ]
                    )
                ),
                MethodDecl(
                    is_static=True,
                    return_type=PrimitiveType("void"),
                    name="main",
                    params=[],
                    body=BlockStatement(
                        var_decls=[
                            VariableDecl(
                                is_final=False,
                                var_type=ArrayType(
                                    element_type=PrimitiveType("int"),
                                    size=2
                                ),
                                variables=[
                                    Variable(
                                        name="a",
                                        init_value=ArrayLiteral(
                                            elements=[
                                                IntLiteral(0),
                                                IntLiteral(0)
                                            ]
                                        )
                                    )
                                ]
                            )
                        ],
                        statements=[
                            MethodInvocationStatement(
                                PostfixExpression(
                                    primary=Identifier("Main"),
                                    postfix_ops=[
                                        MethodCall(
                                            method_name="foo",
                                            args=[Identifier("a")]
                                        )
                                    ]
                                )
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    primary=Identifier("io"),
                                    postfix_ops=[
                                        MethodCall(
                                            method_name="writeInt",
                                            args=[
                                                PostfixExpression(
                                                    primary=Identifier("a"),
                                                    postfix_ops=[
                                                        ArrayAccess(index=IntLiteral(1))
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "2"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_096():
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    is_static=True,
                    return_type=PrimitiveType("void"),
                    name="main",
                    params=[],
                    body=BlockStatement(
                        var_decls=[
                            VariableDecl(
                                is_final=False,
                                var_type=ArrayType(
                                    element_type=PrimitiveType("boolean"),
                                    size=2
                                ),
                                variables=[
                                    Variable(
                                        name="a",
                                        init_value=ArrayLiteral(
                                            elements=[
                                                BoolLiteral(True),
                                                BoolLiteral(False)
                                            ]
                                        )
                                    )
                                ]
                            ),
                            VariableDecl(
                                is_final=False,
                                var_type=ArrayType(
                                    element_type=PrimitiveType("float"),
                                    size=2
                                ),
                                variables=[
                                    Variable(
                                        name="b",
                                        init_value=ArrayLiteral(
                                            elements=[
                                                FloatLiteral(3.14),
                                                FloatLiteral(2.56)
                                            ]
                                        )
                                    )
                                ]
                            ),
                            VariableDecl(
                                is_final=False,
                                var_type=ArrayType(
                                    element_type=PrimitiveType("string"),
                                    size=2
                                ),
                                variables=[
                                    Variable(
                                        name="c",
                                        init_value=ArrayLiteral(
                                            elements=[
                                                StringLiteral("Hello"),
                                                StringLiteral("Hey")
                                            ]
                                        )
                                    )
                                ]
                            )
                        ],
                        statements=[
                            MethodInvocationStatement(
                                PostfixExpression(
                                    primary=Identifier("io"),
                                    postfix_ops=[
                                        MethodCall(
                                            method_name="writeBool",
                                            args=[
                                                PostfixExpression(
                                                    primary=Identifier("a"),
                                                    postfix_ops=[ArrayAccess(index=IntLiteral(0))]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    primary=Identifier("io"),
                                    postfix_ops=[
                                        MethodCall(
                                            method_name="writeBool",
                                            args=[
                                                PostfixExpression(
                                                    primary=Identifier("a"),
                                                    postfix_ops=[
                                                        ArrayAccess(
                                                            index=BinaryOp(
                                                                left=IntLiteral(1),
                                                                operator="*",
                                                                right=IntLiteral(1)
                                                            )
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    primary=Identifier("io"),
                                    postfix_ops=[
                                        MethodCall(
                                            method_name="writeFloat",
                                            args=[
                                                PostfixExpression(
                                                    primary=Identifier("b"),
                                                    postfix_ops=[ArrayAccess(index=IntLiteral(0))]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    primary=Identifier("io"),
                                    postfix_ops=[
                                        MethodCall(
                                            method_name="writeFloat",
                                            args=[
                                                PostfixExpression(
                                                    primary=Identifier("b"),
                                                    postfix_ops=[
                                                        ArrayAccess(
                                                            index=BinaryOp(
                                                                left=IntLiteral(2),
                                                                operator="\\",
                                                                right=IntLiteral(2)
                                                            )
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    primary=Identifier("io"),
                                    postfix_ops=[
                                        MethodCall(
                                            method_name="writeStr",
                                            args=[
                                                PostfixExpression(
                                                    primary=Identifier("c"),
                                                    postfix_ops=[ArrayAccess(index=IntLiteral(0))]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    primary=Identifier("io"),
                                    postfix_ops=[
                                        MethodCall(
                                            method_name="writeStr",
                                            args=[
                                                PostfixExpression(
                                                    primary=Identifier("c"),
                                                    postfix_ops=[
                                                        ArrayAccess(
                                                            index=BinaryOp(
                                                                left=IntLiteral(0),
                                                                operator="+",
                                                                right=IntLiteral(1)
                                                            )
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "truefalse3.142.56HelloHey"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_097():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("a", IntLiteral(10))]),
                    VariableDecl(False, PrimitiveType("int"), [Variable("b", IntLiteral(5))])
                ], 
                [
                    IfStatement(
                        BinaryOp(
                            BinaryOp(
                                BinaryOp(ParenthesizedExpression(BinaryOp(Identifier("a"), "+", Identifier("b"))), "*", IntLiteral(2)),
                                ">",
                                IntLiteral(25)
                            ),
                            "&&",
                            BinaryOp(
                                ParenthesizedExpression(BinaryOp(Identifier("a"), "-", Identifier("b"))),
                                "<",
                                IntLiteral(10)
                            )
                        ),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStr", [StringLiteral("Pass")])])),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStr", [StringLiteral("Fail")])]))
                    )
                ]
            ))
        ])
    ])
    expected = "Pass"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_098():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("sum", IntLiteral(0))]),
                    VariableDecl(False, PrimitiveType("int"), [Variable("i", None)])
                ], 
                [
                    ForStatement("i", IntLiteral(1), "to", IntLiteral(5), BlockStatement([], [
                        AssignmentStatement(IdLHS("sum"), BinaryOp(Identifier("sum"), "+", Identifier("i")))
                    ])),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeInt", [Identifier("sum")])]))
                ]
            ))
        ])
    ])
    expected = "15"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_099():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("f", IntLiteral(1))]),
                    VariableDecl(False, PrimitiveType("int"), [Variable("i", None)])
                ], 
                [
                    ForStatement("i", IntLiteral(1), "to", IntLiteral(5), BlockStatement([], [
                        AssignmentStatement(IdLHS("f"), BinaryOp(Identifier("f"), "*", Identifier("i")))
                    ])),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeInt", [Identifier("f")])]))
                ]
            ))
        ])
    ])
    expected = "120"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_100():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("count", IntLiteral(0))]),
                    VariableDecl(False, PrimitiveType("int"), [Variable("i", None)])
                ], 
                [
                    ForStatement("i", IntLiteral(1), "to", IntLiteral(6), BlockStatement([], [
                        IfStatement(
                            BinaryOp(BinaryOp(Identifier("i"), "%", IntLiteral(2)), "==", IntLiteral(0)),
                            AssignmentStatement(IdLHS("count"), BinaryOp(Identifier("count"), "+", IntLiteral(1))),
                            None
                        )
                    ])),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeInt", [Identifier("count")])]))
                ]
            ))
        ])
    ])
    expected = "3"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_101():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("a", IntLiteral(0))]),
                    VariableDecl(False, PrimitiveType("int"), [Variable("b", IntLiteral(1))]),
                    VariableDecl(False, PrimitiveType("int"), [Variable("temp", IntLiteral(0))]),
                    VariableDecl(False, PrimitiveType("int"), [Variable("i", None)])
                ], 
                [
                    ForStatement("i", IntLiteral(1), "to", IntLiteral(5), BlockStatement([], [
                        AssignmentStatement(IdLHS("temp"), BinaryOp(Identifier("a"), "+", Identifier("b"))),
                        AssignmentStatement(IdLHS("a"), Identifier("b")),
                        AssignmentStatement(IdLHS("b"), Identifier("temp"))
                    ])),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeInt", [Identifier("a")])]))
                ]
            ))
        ])
    ])
    expected = "5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_102():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("i", None)]),
                    VariableDecl(False, PrimitiveType("int"), [Variable("limit", IntLiteral(3))])
                ], 
                [
                    ForStatement("i", IntLiteral(1), "to", Identifier("limit"), BlockStatement([], [
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeInt", [Identifier("i")])
                        ])),
                        AssignmentStatement(IdLHS("limit"), IntLiteral(100))
                    ]))
                ]
            ))
        ])
    ])
    expected = "123"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_103():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("i", None)]),
                    VariableDecl(False, PrimitiveType("int"), [Variable("sum", IntLiteral(0))])
                ], 
                [
                    ForStatement("i", IntLiteral(1), "to", IntLiteral(5), BlockStatement([], [
                        AssignmentStatement(IdLHS("sum"), BinaryOp(Identifier("sum"), "+", Identifier("i"))),
                        IfStatement(
                            BinaryOp(Identifier("sum"), ">", IntLiteral(10)),
                            BreakStatement(),
                            None
                        )
                    ])),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeInt", [Identifier("sum")])]))
                ]
            ))
        ])
    ])
    expected = "15"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_104():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, PrimitiveType("int"), [Variable("i", None)])], 
                [
                    ForStatement("i", IntLiteral(1), "to", IntLiteral(5), BlockStatement([], [
                        IfStatement(
                            BinaryOp(Identifier("i"), "==", IntLiteral(3)),
                            BreakStatement(),
                            None
                        ),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeInt", [Identifier("i")])
                        ]))
                    ]))
                ]
            ))
        ])
    ])
    expected = "12"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_105():
    # ast = """
    # class X {
    #     static void main() {
    #         int a := 1;
    #         a := 2;
    #         io.writeInt(a);         
    #     }
    # }
    # """
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("a", IntLiteral(1))])
                ], 
                [
                    AssignmentStatement(IdLHS("a"), IntLiteral(2)),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                        MethodCall("writeInt", [Identifier("a")])
                    ]))
                ]
            ))
        ])
    ])
    expected = "2"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_106():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("i", None)]),
                    VariableDecl(False, PrimitiveType("int"), [Variable("sum", IntLiteral(0))])
                ], 
                [
                    ForStatement("i", IntLiteral(1), "to", IntLiteral(5), BlockStatement([], [
                        IfStatement(
                            BinaryOp(BinaryOp(Identifier("i"), "%", IntLiteral(2)), "==", IntLiteral(0)),
                            ContinueStatement(),
                            None
                        ),
                        AssignmentStatement(IdLHS("sum"), BinaryOp(Identifier("sum"), "+", Identifier("i")))
                    ])),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeInt", [Identifier("sum")])]))
                ]
            ))
        ])
    ])
    expected = "9"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_107():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("i", None)]),
                    VariableDecl(False, PrimitiveType("int"), [Variable("sum", IntLiteral(0))])
                ], 
                [
                    ForStatement("i", IntLiteral(1), "to", IntLiteral(5), BlockStatement([], [
                        IfStatement(
                            BinaryOp(BinaryOp(Identifier("i"), "%", IntLiteral(2)), "==", IntLiteral(1)),
                            ContinueStatement(),
                            None
                        ),
                        AssignmentStatement(IdLHS("sum"), BinaryOp(Identifier("sum"), "+", Identifier("i")))
                    ])),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeInt", [Identifier("sum")])]))
                ]
            ))
        ])
    ])
    expected = "6"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_108():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("i", None)]),
                    VariableDecl(False, PrimitiveType("int"), [Variable("sum", IntLiteral(0))])
                ], 
                [
                    ForStatement("i", IntLiteral(1), "to", IntLiteral(5), BlockStatement([], [
                        IfStatement(
                            BinaryOp(Identifier("i"), "==", IntLiteral(3)),
                            ContinueStatement(),
                            None
                        ),
                        AssignmentStatement(IdLHS("sum"), BinaryOp(Identifier("sum"), "+", Identifier("i")))
                    ])),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeInt", [Identifier("sum")])]))
                ]
            ))
        ])
    ])
    expected = "12"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_109():
#     ast = """
# class X {
#     static void main() {
#         int a := 1;
#         {
#             int a;
#             a := 2;
#             io.writeInt(a);  
#         }
#         io.writeInt(a);         
#     }
# }
# """
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("a", IntLiteral(1))])
                ], 
                [
                    BlockStatement(
                        [
                            VariableDecl(False, PrimitiveType("int"), [Variable("a", None)])
                        ], 
                        [
                            AssignmentStatement(IdLHS("a"), IntLiteral(2)),
                            MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                                MethodCall("writeInt", [Identifier("a")])
                            ]))
                        ]
                    ),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                        MethodCall("writeInt", [Identifier("a")])
                    ]))
                ]
            ))
        ])
    ])
    expected = "21"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_110():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("a", IntLiteral(1))])
                ], 
                [
                    BlockStatement(
                        [
                            VariableDecl(False, PrimitiveType("int"), [Variable("b", IntLiteral(2))])
                        ], 
                        [
                            MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                                MethodCall("writeInt", [Identifier("a")])
                            ])),
                            MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                                MethodCall("writeInt", [Identifier("b")])
                            ]))
                        ]
                    ),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                        MethodCall("writeInt", [Identifier("a")])
                    ]))
                ]
            ))
        ])
    ])
    expected = "121"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected
def test_111():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("a", IntLiteral(1))])
                ], 
                [
                    BlockStatement(
                        [
                            VariableDecl(False, PrimitiveType("int"), [Variable("a", IntLiteral(2))])
                        ], 
                        [
                            MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                                MethodCall("writeInt", [Identifier("a")])
                            ]))
                        ]
                    ),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                        MethodCall("writeInt", [Identifier("a")])
                    ]))
                ]
            ))
        ])
    ])
    expected = "21"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected
def test_112():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("a", IntLiteral(1))])
                ], 
                [
                    BlockStatement(
                        [
                            VariableDecl(False, PrimitiveType("int"), [Variable("b", IntLiteral(2))])
                        ], 
                        [
                            BlockStatement(
                                [
                                    VariableDecl(False, PrimitiveType("int"), [Variable("c", IntLiteral(3))])
                                ],
                                [
                                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                                        MethodCall("writeInt", [Identifier("a")])
                                    ])),
                                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                                        MethodCall("writeInt", [Identifier("b")])
                                    ])),
                                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                                        MethodCall("writeInt", [Identifier("c")])
                                    ]))
                                ]
                            )
                        ]
                    ),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                        MethodCall("writeInt", [Identifier("a")])
                    ]))
                ]
            ))
        ])
    ])
    expected = "1231"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_113():
#     ast = """
# class X {
#     static void foo(int a){
#         io.writeInt(a);
#         a := 1;
#         io.writeInt(a);
#     }
#     static void main() {
#         int a := 2;
#         X.foo(a);
#         io.writeInt(a);      
#     }
# }
# """
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "foo",
                    [
                        Parameter(
                            PrimitiveType("int"),
                            "a"
                        )
                    ],
                    BlockStatement(
                        [],
                        [
                            MethodInvocationStatement(
                                PostfixExpression(
                                    Identifier("io"),
                                    [
                                        MethodCall(
                                            "writeInt",
                                            [Identifier("a")]
                                        )
                                    ]
                                )
                            ),
                            AssignmentStatement(
                                IdLHS("a"),
                                IntLiteral(1)
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    Identifier("io"),
                                    [
                                        MethodCall(
                                            "writeInt",
                                            [Identifier("a")]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ),
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement(
                        [
                            VariableDecl(
                                False,
                                PrimitiveType("int"),
                                [
                                    Variable(
                                        "a",
                                        IntLiteral(2)
                                    )
                                ]
                            )
                        ],
                        [
                            MethodInvocationStatement(
                                PostfixExpression(
                                    Identifier("Main"),
                                    [
                                        MethodCall(
                                            "foo",
                                            [Identifier("a")]
                                        )
                                    ]
                                )
                            ),
                            MethodInvocationStatement(
                                PostfixExpression(
                                    Identifier("io"),
                                    [
                                        MethodCall(
                                            "writeInt",
                                            [Identifier("a")]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    ])
    expected = "212"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_114():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("a", IntLiteral(10))])
                ], 
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                        MethodCall("writeInt", [Identifier("a")])
                    ])),
                    AssignmentStatement(IdLHS("a"), IntLiteral(20)),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                        MethodCall("writeInt", [Identifier("a")])
                    ]))
                ]
            ))
        ])
    ])
    expected = "1020"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_115():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("a", IntLiteral(10))])
                ], 
                [
                    BlockStatement(
                        [],
                        [
                            AssignmentStatement(IdLHS("a"), IntLiteral(30)),
                            MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                                MethodCall("writeInt", [Identifier("a")])
                            ]))
                        ]
                    ),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                        MethodCall("writeInt", [Identifier("a")])
                    ]))
                ]
            ))
        ])
    ])
    expected = "3030"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_116():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("a", IntLiteral(10))])
                ], 
                [
                    BlockStatement(
                        [
                            VariableDecl(False, PrimitiveType("int"), [Variable("a", IntLiteral(40))])
                        ],
                        [
                            MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                                MethodCall("writeInt", [Identifier("a")])
                            ]))
                        ]
                    ),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                        MethodCall("writeInt", [Identifier("a")])
                    ]))
                ]
            ))
        ])
    ])
    expected = "4010"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_117():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("a", IntLiteral(10))])
                ], 
                [
                    BlockStatement(
                        [
                            VariableDecl(False, PrimitiveType("int"), [Variable("b", IntLiteral(50))])
                        ],
                        [
                            MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                                MethodCall("writeInt", [Identifier("a")])
                            ])),
                            MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                                MethodCall("writeInt", [Identifier("b")])
                            ]))
                        ]
                    ),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                        MethodCall("writeInt", [Identifier("a")])
                    ]))
                ]
            ))
        ])
    ])
    expected = "105010"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_118():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("a", IntLiteral(10))])
                ], 
                [
                    BlockStatement(
                        [
                            VariableDecl(False, PrimitiveType("int"), [Variable("a", IntLiteral(60))])
                        ],
                        [
                            MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                                MethodCall("writeInt", [Identifier("a")])
                            ]))
                        ]
                    ),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                        MethodCall("writeInt", [Identifier("a")])
                    ]))
                ]
            ))
        ])
    ])
    expected = "6010"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_119():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("a", IntLiteral(10))])
                ], 
                [
                    BlockStatement(
                        [
                            VariableDecl(False, PrimitiveType("int"), [Variable("b", IntLiteral(70))])
                        ],
                        [
                            MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                                MethodCall("writeInt", [Identifier("a")])
                            ])),
                            MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                                MethodCall("writeInt", [Identifier("b")])
                            ]))
                        ]
                    ),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                        MethodCall("writeInt", [Identifier("a")])
                    ]))
                ]
            ))
        ])
    ])
    expected = "107010"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

# test if statement
def test_120():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("a", IntLiteral(10))])
                ], 
                [
                    IfStatement(
                        BinaryOp(Identifier("a"), ">", IntLiteral(5)),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeStr", [StringLiteral("Greater")]
                        )])),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeStr", [StringLiteral("Not Greater")]
                        )]))
                    )
                ]
            ))
        ])
    ])
    expected = "Greater"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected
def test_121():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("a", IntLiteral(3))])
                ], 
                [
                    IfStatement(
                        BinaryOp(Identifier("a"), "<", IntLiteral(5)),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeStr", [StringLiteral("Less")]
                        )])),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeStr", [StringLiteral("Not Less")]
                        )]))
                    )
                ]
            ))
        ])
    ])
    expected = "Less"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected
def test_122():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("a", IntLiteral(7))])
                ], 
                [
                    IfStatement(
                        BinaryOp(Identifier("a"), "==", IntLiteral(10)),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeStr", [StringLiteral("Equal")]
                        )])),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeStr", [StringLiteral("Not Equal")]
                        )]))
                    )
                ]
            ))
        ])
    ])
    expected = "Not Equal"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected
def test_123():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("a", IntLiteral(8))]),
                    VariableDecl(False, PrimitiveType("int"), [Variable("b", IntLiteral(12))])
                ], 
                [
                    IfStatement(
                        BinaryOp(
                            BinaryOp(
                                Identifier("a"),
                                ">=",
                                IntLiteral(5)
                            ),
                            "&&",
                            BinaryOp(
                                Identifier("b"),
                                "<=",
                                IntLiteral(15)
                            )
                        ),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeStr", [StringLiteral("Both True")]
                        )])),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeStr", [StringLiteral("At least one False")]
                        )]))
                    )
                ]
            ))
        ])
    ])
    expected = "Both True"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected
def test_124():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("a", IntLiteral(4))]),
                    VariableDecl(False, PrimitiveType("int"), [Variable("b", IntLiteral(20))])
                ], 
                [
                    IfStatement(
                        BinaryOp(
                            BinaryOp(
                                Identifier("a"),
                                "<=",
                                IntLiteral(3)
                            ),
                            "||",
                            BinaryOp(
                                Identifier("b"),
                                ">=",
                                IntLiteral(15)
                            )
                        ),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeStr", [StringLiteral("At least one True")]
                        )])),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeStr", [StringLiteral("Both False")]
                        )]))
                    )
                ]
            ))
        ])
    ])
    expected = "At least one True"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_125():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("a", IntLiteral(10))])
                ], 
                [
                    IfStatement(
                        BinaryOp(Identifier("a"), "<", IntLiteral(5)),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeStr", [StringLiteral("Less")]
                        )])),
                        IfStatement(
                            BinaryOp(Identifier("a"), "==", IntLiteral(10)),
                            MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                                MethodCall("writeStr", [StringLiteral("Equal")]
                            )])),
                            MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                                MethodCall("writeStr", [StringLiteral("Greater")]
                            )]))
                        )
                    )
                ]
            ))
        ])
    ])
    expected = "Equal"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

# test for statement
def test_126():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("i", None)])
                ], 
                [
                    ForStatement("i", IntLiteral(1), "to", IntLiteral(5), BlockStatement([], [
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeInt", [Identifier("i")])
                        ]))
                    ]))
                ]
            ))
        ])
    ])
    expected = "12345"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_127():
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("i", None)])
                ], 
                [
                    ForStatement("i", IntLiteral(5), "downto", IntLiteral(1), BlockStatement([], [
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeInt", [Identifier("i")])
                        ]))
                    ]))
                ]
            ))
        ])
    ])
    expected = "54321"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_128():
    """Test modulo operation"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [BinaryOp(IntLiteral(10), "%", IntLiteral(3))])
                ]))
            ]))
        ])
    ])
    expected = "1"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_129():
    """Test equality comparison"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [BinaryOp(IntLiteral(5), "==", IntLiteral(5))])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_130():
    """Test inequality comparison"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [BinaryOp(IntLiteral(5), "!=", IntLiteral(3))])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_131():
    """Test less than comparison"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [BinaryOp(IntLiteral(3), "<", IntLiteral(5))])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_132():
    """Test greater than or equal comparison"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [BinaryOp(IntLiteral(5), ">=", IntLiteral(5))])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_133():
    """Test less than or equal comparison"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [BinaryOp(IntLiteral(3), "<=", IntLiteral(5))])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_134():
    """Test logical AND"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [BinaryOp(BoolLiteral(True), "&&", BoolLiteral(True))])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_135():
    """Test logical OR"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [BinaryOp(BoolLiteral(False), "||", BoolLiteral(True))])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_136():
    """Test nested for loops"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, PrimitiveType("int"), [Variable("i", None)]),
                VariableDecl(False, PrimitiveType("int"), [Variable("j", None)])
            ], [
                ForStatement("i", IntLiteral(1), "to", IntLiteral(2), 
                    ForStatement("j", IntLiteral(1), "to", IntLiteral(2),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeInt", [BinaryOp(Identifier("i"), "+", Identifier("j"))])
                        ]))
                    )
                )
            ]))
        ])
    ])
    expected = "2334"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_137():
    """Test break in for loop"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, PrimitiveType("int"), [Variable("i", None)])
            ], [
                ForStatement("i", IntLiteral(1), "to", IntLiteral(5),
                    BlockStatement([], [
                        IfStatement(BinaryOp(Identifier("i"), "==", IntLiteral(3)), BreakStatement(), None),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeInt", [Identifier("i")])
                        ]))
                    ])
                )
            ]))
        ])
    ])
    expected = "12"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_138():
    """Test continue in for loop"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, PrimitiveType("int"), [Variable("i", None)])
            ], [
                ForStatement("i", IntLiteral(1), "to", IntLiteral(5),
                    BlockStatement([], [
                        IfStatement(BinaryOp(Identifier("i"), "==", IntLiteral(3)), ContinueStatement(), None),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeInt", [Identifier("i")])
                        ]))
                    ])
                )
            ]))
        ])
    ])
    expected = "1245"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_139():
    """Test if-else statement"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, PrimitiveType("int"), [Variable("x", IntLiteral(3))])
            ], [
                IfStatement(
                    BinaryOp(Identifier("x"), ">", IntLiteral(5)),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                        MethodCall("writeStr", [StringLiteral("big")])
                    ])),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                        MethodCall("writeStr", [StringLiteral("small")])
                    ]))
                )
            ]))
        ])
    ])
    expected = "small"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_140():
    """Test method with return value"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("int"), "add", [
                Parameter(PrimitiveType("int"), "a"),
                Parameter(PrimitiveType("int"), "b")
            ], BlockStatement([], [
                ReturnStatement(BinaryOp(Identifier("a"), "+", Identifier("b")))
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        PostfixExpression(Identifier("Main"), [
                            MethodCall("add", [IntLiteral(10), IntLiteral(20)])
                        ])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "30"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_141():
    """Test method with multiple parameters"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("int"), "multiply", [
                Parameter(PrimitiveType("int"), "a"),
                Parameter(PrimitiveType("int"), "b"),
                Parameter(PrimitiveType("int"), "c")
            ], BlockStatement([], [
                ReturnStatement(BinaryOp(BinaryOp(Identifier("a"), "*", Identifier("b")), "*", Identifier("c")))
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        PostfixExpression(Identifier("Main"), [
                            MethodCall("multiply", [IntLiteral(2), IntLiteral(3), IntLiteral(4)])
                        ])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "24"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_142():
    """Test array of floats"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ArrayType(PrimitiveType("float"), 3), [
                    Variable("arr", ArrayLiteral([FloatLiteral(1.1), FloatLiteral(2.2), FloatLiteral(3.3)]))
                ])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeFloat", [
                        PostfixExpression(Identifier("arr"), [ArrayAccess(IntLiteral(1))])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "2.2"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_143():
    """Test array of strings"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ArrayType(PrimitiveType("string"), 2), [
                    Variable("arr", ArrayLiteral([StringLiteral("Hello"), StringLiteral("World")]))
                ])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeStr", [
                        PostfixExpression(Identifier("arr"), [ArrayAccess(IntLiteral(0))])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "Hello"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_144():
    """Test float addition"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeFloat", [BinaryOp(FloatLiteral(1.5), "+", FloatLiteral(2.5))])
                ]))
            ]))
        ])
    ])
    expected = "4.0"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_145():
    """Test float multiplication"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeFloat", [BinaryOp(FloatLiteral(2.0), "*", FloatLiteral(3.0))])
                ]))
            ]))
        ])
    ])
    expected = "6.0"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_146():
    """Test complex expression with precedence"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        BinaryOp(
                            BinaryOp(IntLiteral(2), "+", IntLiteral(3)),
                            "*",
                            BinaryOp(IntLiteral(4), "+", IntLiteral(5))
                        )
                    ])
                ]))
            ]))
        ])
    ])
    expected = "45"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_147():
    """Test multiple variable declarations"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, PrimitiveType("int"), [
                    Variable("a", IntLiteral(1)),
                    Variable("b", IntLiteral(2)),
                    Variable("c", IntLiteral(3))
                ])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [BinaryOp(BinaryOp(Identifier("a"), "+", Identifier("b")), "+", Identifier("c"))])
                ]))
            ]))
        ])
    ])
    expected = "6"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected





def test_149():
    """Test object creation and method call"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(False, PrimitiveType("int"), "getValue", [], BlockStatement([], [
                ReturnStatement(IntLiteral(42))
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("Main"), [Variable("m", ObjectCreation("Main", []))])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        PostfixExpression(Identifier("m"), [MethodCall("getValue", [])])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_150():
    """Test this expression in instance method"""
    ast = Program([
        ClassDecl("Main", None, [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("value", None)]),
            MethodDecl(False, PrimitiveType("void"), "setValue", [
                Parameter(PrimitiveType("int"), "v")
            ], BlockStatement([], [
                AssignmentStatement(
                    PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("value")])),
                    Identifier("v")
                )
            ])),
            MethodDecl(False, PrimitiveType("int"), "getValue", [], BlockStatement([], [
                ReturnStatement(PostfixExpression(ThisExpression(), [MemberAccess("value")]))
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("Main"), [Variable("m", ObjectCreation("Main", []))])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("m"), [
                    MethodCall("setValue", [IntLiteral(100)])
                ])),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        PostfixExpression(Identifier("m"), [MethodCall("getValue", [])])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "100"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_151():
    """Test static attribute"""
    ast = Program([
        ClassDecl("Main", None, [
            AttributeDecl(True, False, PrimitiveType("int"), [Attribute("counter", IntLiteral(0))]),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                AssignmentStatement(
                    PostfixLHS(PostfixExpression(Identifier("Main"), [MemberAccess("counter")])),
                    IntLiteral(5)
                ),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        PostfixExpression(Identifier("Main"), [MemberAccess("counter")])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_152():
    """Test parenthesized expression"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        BinaryOp(
                            ParenthesizedExpression(BinaryOp(IntLiteral(2), "+", IntLiteral(3))),
                            "*",
                            IntLiteral(4)
                        )
                    ])
                ]))
            ]))
        ])
    ])
    expected = "20"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_153():
    """Test string concatenation in loop"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, PrimitiveType("int"), [Variable("i", None)]),
                VariableDecl(False, PrimitiveType("string"), [Variable("s", StringLiteral(""))])
            ], [
                ForStatement("i", IntLiteral(1), "to", IntLiteral(3),
                    AssignmentStatement(IdLHS("s"), BinaryOp(Identifier("s"), "^", StringLiteral("a")))
                ),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeStr", [Identifier("s")])
                ]))
            ]))
        ])
    ])
    expected = "aaa"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_154():
    """Test factorial calculation"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("int"), "factorial", [
                Parameter(PrimitiveType("int"), "n")
            ], BlockStatement([], [
                IfStatement(
                    BinaryOp(Identifier("n"), "<=", IntLiteral(1)),
                    ReturnStatement(IntLiteral(1)),
                    ReturnStatement(BinaryOp(
                        Identifier("n"),
                        "*",
                        PostfixExpression(Identifier("Main"), [
                            MethodCall("factorial", [BinaryOp(Identifier("n"), "-", IntLiteral(1))])
                        ])
                    ))
                )
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        PostfixExpression(Identifier("Main"), [MethodCall("factorial", [IntLiteral(5)])])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "120"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_155():
    """Test boolean variable"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, PrimitiveType("boolean"), [Variable("flag", BoolLiteral(False))])
            ], [
                AssignmentStatement(IdLHS("flag"), BoolLiteral(True)),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [Identifier("flag")])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_156():
    """Test unary plus"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [UnaryOp("+", IntLiteral(42))])
                ]))
            ]))
        ])
    ])
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_157():
    """Test complex boolean expression"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [
                        BinaryOp(
                            BinaryOp(IntLiteral(5), ">", IntLiteral(3)),
                            "&&",
                            BinaryOp(IntLiteral(10), "<", IntLiteral(20))
                        )
                    ])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_158():
    """Test array length in loop"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ArrayType(PrimitiveType("int"), 5), [
                    Variable("arr", ArrayLiteral([
                        IntLiteral(10), IntLiteral(20), IntLiteral(30), IntLiteral(40), IntLiteral(50)
                    ]))
                ]),
                VariableDecl(False, PrimitiveType("int"), [Variable("sum", IntLiteral(0))]),
                VariableDecl(False, PrimitiveType("int"), [Variable("i", None)])
            ], [
                ForStatement("i", IntLiteral(0), "to", IntLiteral(4),
                    AssignmentStatement(
                        IdLHS("sum"),
                        BinaryOp(
                            Identifier("sum"),
                            "+",
                            PostfixExpression(Identifier("arr"), [ArrayAccess(Identifier("i"))])
                        )
                    )
                ),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [Identifier("sum")])
                ]))
            ]))
        ])
    ])
    expected = "150"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_159():
    """Test final variable"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(True, PrimitiveType("int"), [Variable("MAX", IntLiteral(100))])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [Identifier("MAX")])
                ]))
            ]))
        ])
    ])
    expected = "100"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_160():
    """Test multiple objects"""
    ast = Program([
        ClassDecl("Main", None, [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("x", None)]),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("Main"), [Variable("m1", ObjectCreation("Main", []))]),
                VariableDecl(False, ClassType("Main"), [Variable("m2", ObjectCreation("Main", []))])
            ], [
                AssignmentStatement(
                    PostfixLHS(PostfixExpression(Identifier("m1"), [MemberAccess("x")])),
                    IntLiteral(10)
                ),
                AssignmentStatement(
                    PostfixLHS(PostfixExpression(Identifier("m2"), [MemberAccess("x")])),
                    IntLiteral(20)
                ),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        BinaryOp(
                            PostfixExpression(Identifier("m1"), [MemberAccess("x")]),
                            "+",
                            PostfixExpression(Identifier("m2"), [MemberAccess("x")])
                        )
                    ])
                ]))
            ]))
        ])
    ])
    expected = "30"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_161():
    """Test nested if-else"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, PrimitiveType("int"), [Variable("score", IntLiteral(85))])
            ], [
                IfStatement(
                    BinaryOp(Identifier("score"), ">=", IntLiteral(90)),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                        MethodCall("writeStr", [StringLiteral("A")])
                    ])),
                    IfStatement(
                        BinaryOp(Identifier("score"), ">=", IntLiteral(80)),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeStr", [StringLiteral("B")])
                        ])),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeStr", [StringLiteral("C")])
                        ]))
                    )
                )
            ]))
        ])
    ])
    expected = "B"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_162():
    """Test float comparison"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [BinaryOp(FloatLiteral(3.14), ">", FloatLiteral(2.5))])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_163():
    """Test method with float return type"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("float"), "average", [
                Parameter(PrimitiveType("float"), "a"),
                Parameter(PrimitiveType("float"), "b")
            ], BlockStatement([], [
                ReturnStatement(BinaryOp(BinaryOp(Identifier("a"), "+", Identifier("b")), "/", FloatLiteral(2.0)))
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeFloat", [
                        PostfixExpression(Identifier("Main"), [
                            MethodCall("average", [FloatLiteral(10.0), FloatLiteral(20.0)])
                        ])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "15.0"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_165():
    """Test method with boolean return"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("boolean"), "isPositive", [
                Parameter(PrimitiveType("int"), "n")
            ], BlockStatement([], [
                ReturnStatement(BinaryOp(Identifier("n"), ">", IntLiteral(0)))
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [
                        PostfixExpression(Identifier("Main"), [MethodCall("isPositive", [IntLiteral(5)])])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_166():
    """Test method with string return"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("string"), "greet", [
                Parameter(PrimitiveType("string"), "name")
            ], BlockStatement([], [
                ReturnStatement(BinaryOp(StringLiteral("Hello "), "^", Identifier("name")))
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeStr", [
                        PostfixExpression(Identifier("Main"), [MethodCall("greet", [StringLiteral("World")])])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "Hello World"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_167():
    """Test downto loop with step"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, PrimitiveType("int"), [Variable("i", None)])
            ], [
                ForStatement("i", IntLiteral(10), "downto", IntLiteral(8),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                        MethodCall("writeInt", [Identifier("i")])
                    ]))
                )
            ]))
        ])
    ])
    expected = "1098"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_168():
    """Test array assignment in loop"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ArrayType(PrimitiveType("int"), 3), [
                    Variable("arr", ArrayLiteral([IntLiteral(0), IntLiteral(0), IntLiteral(0)]))
                ]),
                VariableDecl(False, PrimitiveType("int"), [Variable("i", None)])
            ], [
                ForStatement("i", IntLiteral(0), "to", IntLiteral(2),
                    AssignmentStatement(
                        PostfixLHS(PostfixExpression(Identifier("arr"), [ArrayAccess(Identifier("i"))])),
                        BinaryOp(Identifier("i"), "*", IntLiteral(2))
                    )
                ),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [PostfixExpression(Identifier("arr"), [ArrayAccess(IntLiteral(0))])])
                ])),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [PostfixExpression(Identifier("arr"), [ArrayAccess(IntLiteral(1))])])
                ])),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [PostfixExpression(Identifier("arr"), [ArrayAccess(IntLiteral(2))])])
                ]))
            ]))
        ])
    ])
    expected = "024"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_169():
    """Test complex arithmetic"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        BinaryOp(
                            BinaryOp(IntLiteral(100), "-", IntLiteral(50)),
                            "+",
                            BinaryOp(IntLiteral(10), "*", IntLiteral(5))
                        )
                    ])
                ]))
            ]))
        ])
    ])
    expected = "100"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_170():
    """Test multiple method calls in sequence"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "printNum", [
                Parameter(PrimitiveType("int"), "n")
            ], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [Identifier("n")])
                ]))
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("Main"), [
                    MethodCall("printNum", [IntLiteral(1)])
                ])),
                MethodInvocationStatement(PostfixExpression(Identifier("Main"), [
                    MethodCall("printNum", [IntLiteral(2)])
                ])),
                MethodInvocationStatement(PostfixExpression(Identifier("Main"), [
                    MethodCall("printNum", [IntLiteral(3)])
                ]))
            ]))
        ])
    ])
    expected = "123"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_171():
    """Test boolean AND with false"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [BinaryOp(BoolLiteral(True), "&&", BoolLiteral(False))])
                ]))
            ]))
        ])
    ])
    expected = "false"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_172():
    """Test boolean OR with false"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [BinaryOp(BoolLiteral(False), "||", BoolLiteral(False))])
                ]))
            ]))
        ])
    ])
    expected = "false"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_173():
    """Test negation of comparison"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [
                        UnaryOp("!", BinaryOp(IntLiteral(5), ">", IntLiteral(10)))
                    ])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_174():
    """Test chained comparison"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, PrimitiveType("int"), [Variable("x", IntLiteral(5))])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [
                        BinaryOp(
                            BinaryOp(IntLiteral(1), "<", Identifier("x")),
                            "&&",
                            BinaryOp(Identifier("x"), "<", IntLiteral(10))
                        )
                    ])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_175():
    """Test sum of array elements"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("int"), "sumArray", [
                Parameter(ArrayType(PrimitiveType("int"), 3), "arr")
            ], BlockStatement([
                VariableDecl(False, PrimitiveType("int"), [Variable("sum", IntLiteral(0))]),
                VariableDecl(False, PrimitiveType("int"), [Variable("i", None)])
            ], [
                ForStatement("i", IntLiteral(0), "to", IntLiteral(2),
                    AssignmentStatement(
                        IdLHS("sum"),
                        BinaryOp(
                            Identifier("sum"),
                            "+",
                            PostfixExpression(Identifier("arr"), [ArrayAccess(Identifier("i"))])
                        )
                    )
                ),
                ReturnStatement(Identifier("sum"))
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ArrayType(PrimitiveType("int"), 3), [
                    Variable("numbers", ArrayLiteral([IntLiteral(10), IntLiteral(20), IntLiteral(30)]))
                ])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        PostfixExpression(Identifier("Main"), [
                            MethodCall("sumArray", [Identifier("numbers")])
                        ])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "60"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_176():
    """Test counter increment"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, PrimitiveType("int"), [Variable("count", IntLiteral(0))])
            ], [
                AssignmentStatement(IdLHS("count"), BinaryOp(Identifier("count"), "+", IntLiteral(1))),
                AssignmentStatement(IdLHS("count"), BinaryOp(Identifier("count"), "+", IntLiteral(1))),
                AssignmentStatement(IdLHS("count"), BinaryOp(Identifier("count"), "+", IntLiteral(1))),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [Identifier("count")])
                ]))
            ]))
        ])
    ])
    expected = "3"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_177():
    """Test max of two numbers"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("int"), "max", [
                Parameter(PrimitiveType("int"), "a"),
                Parameter(PrimitiveType("int"), "b")
            ], BlockStatement([], [
                IfStatement(
                    BinaryOp(Identifier("a"), ">", Identifier("b")),
                    ReturnStatement(Identifier("a")),
                    ReturnStatement(Identifier("b"))
                )
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        PostfixExpression(Identifier("Main"), [
                            MethodCall("max", [IntLiteral(15), IntLiteral(25)])
                        ])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "25"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_178():
    """Test integer division"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [BinaryOp(IntLiteral(10), "\\", IntLiteral(3))])
                ]))
            ]))
        ])
    ])
    expected = "3"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_179():
    """Test float division"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeFloat", [BinaryOp(FloatLiteral(10.0), "/", FloatLiteral(4.0))])
                ]))
            ]))
        ])
    ])
    expected = "2.5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_180():
    """Test mixed int and float arithmetic"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeFloat", [BinaryOp(IntLiteral(5), "+", FloatLiteral(2.5))])
                ]))
            ]))
        ])
    ])
    expected = "7.5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_181():
    """Test complex expression with precedence"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        BinaryOp(
                            BinaryOp(IntLiteral(2), "*", IntLiteral(3)),
                            "+",
                            BinaryOp(IntLiteral(4), "*", IntLiteral(5))
                        )
                    ])
                ]))
            ]))
        ])
    ])
    expected = "26"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_182():
    """Test unary minus on positive number"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [UnaryOp("-", IntLiteral(42))])
                ]))
            ]))
        ])
    ])
    expected = "-42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_183():
    """Test unary minus on negative number"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [UnaryOp("-", UnaryOp("-", IntLiteral(42)))])
                ]))
            ]))
        ])
    ])
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_184():
    """Test logical NOT with true"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [UnaryOp("!", BoolLiteral(True))])
                ]))
            ]))
        ])
    ])
    expected = "false"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_185():
    """Test logical NOT with false"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [UnaryOp("!", BoolLiteral(False))])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_186():
    """Test string concatenation"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeStr", [BinaryOp(StringLiteral("Hello"), "^", StringLiteral(" World"))])
                ]))
            ]))
        ])
    ])
    expected = "Hello World"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_187():
    """Test multiple string concatenations"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeStr", [
                        BinaryOp(
                            BinaryOp(StringLiteral("A"), "^", StringLiteral("B")),
                            "^",
                            StringLiteral("C")
                        )
                    ])
                ]))
            ]))
        ])
    ])
    expected = "ABC"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_188():
    """Test for loop counting down"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, PrimitiveType("int"), [Variable("i", None)])
            ], [
                ForStatement("i", IntLiteral(3), "downto", IntLiteral(1),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                        MethodCall("writeInt", [Identifier("i")])
                    ]))
                )
            ]))
        ])
    ])
    expected = "321"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_189():
    """Test for loop with single iteration"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, PrimitiveType("int"), [Variable("i", None)])
            ], [
                ForStatement("i", IntLiteral(5), "to", IntLiteral(5),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                        MethodCall("writeInt", [Identifier("i")])
                    ]))
                )
            ]))
        ])
    ])
    expected = "5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_190():
    """Test empty array"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ArrayType(PrimitiveType("int"), 0), [
                    Variable("arr", ArrayLiteral([]))
                ])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeStr", [StringLiteral("ok")])
                ]))
            ]))
        ])
    ])
    expected = "ok"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_191():
    """Test array with single element"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ArrayType(PrimitiveType("int"), 0), [
                    Variable("arr", ArrayLiteral([IntLiteral(42)]))
                ])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        PostfixExpression(Identifier("arr"), [ArrayAccess(IntLiteral(0))])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_192():
    """Test array modification in loop"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ArrayType(PrimitiveType("int"), 0), [
                    Variable("arr", ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]))
                ]),
                VariableDecl(False, PrimitiveType("int"), [Variable("i", None)])
            ], [
                ForStatement("i", IntLiteral(0), "to", IntLiteral(2),
                    AssignmentStatement(
                        PostfixLHS(PostfixExpression(Identifier("arr"), [ArrayAccess(Identifier("i"))])),
                        BinaryOp(
                            PostfixExpression(Identifier("arr"), [ArrayAccess(Identifier("i"))]),
                            "*",
                            IntLiteral(2)
                        )
                    )
                ),
                ForStatement("i", IntLiteral(0), "to", IntLiteral(2),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                        MethodCall("writeInt", [
                            PostfixExpression(Identifier("arr"), [ArrayAccess(Identifier("i"))])
                        ])
                    ]))
                )
            ]))
        ])
    ])
    expected = "246"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_193():
    """Test float array"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ArrayType(PrimitiveType("float"), 0), [
                    Variable("arr", ArrayLiteral([FloatLiteral(1.5), FloatLiteral(2.5)]))
                ])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeFloat", [
                        PostfixExpression(Identifier("arr"), [ArrayAccess(IntLiteral(0))])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "1.5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_194():
    """Test string array"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ArrayType(PrimitiveType("string"), 0), [
                    Variable("arr", ArrayLiteral([StringLiteral("hello"), StringLiteral("world")]))
                ])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeStr", [
                        PostfixExpression(Identifier("arr"), [ArrayAccess(IntLiteral(1))])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "world"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_195():
    """Test method with no parameters returning int"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("int"), "getValue", [], BlockStatement([], [
                ReturnStatement(IntLiteral(100))
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        PostfixExpression(Identifier("Main"), [MethodCall("getValue", [])])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "100"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_196():
    """Test method with multiple parameters"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("int"), "calculate", [
                Parameter(PrimitiveType("int"), "a"),
                Parameter(PrimitiveType("int"), "b"),
                Parameter(PrimitiveType("int"), "c")
            ], BlockStatement([], [
                ReturnStatement(
                    BinaryOp(
                        BinaryOp(Identifier("a"), "+", Identifier("b")),
                        "*",
                        Identifier("c")
                    )
                )
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        PostfixExpression(Identifier("Main"), [
                            MethodCall("calculate", [IntLiteral(2), IntLiteral(3), IntLiteral(4)])
                        ])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "20"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_197():
    """Test nested if statements"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, PrimitiveType("int"), [Variable("x", IntLiteral(5))])
            ], [
                IfStatement(
                    BinaryOp(Identifier("x"), ">", IntLiteral(0)),
                    IfStatement(
                        BinaryOp(Identifier("x"), "<", IntLiteral(10)),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeStr", [StringLiteral("middle")])
                        ])),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeStr", [StringLiteral("high")])
                        ]))
                    ),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                        MethodCall("writeStr", [StringLiteral("low")])
                    ]))
                )
            ]))
        ])
    ])
    expected = "middle"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_198():
    """Test if without else"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, PrimitiveType("int"), [Variable("x", IntLiteral(10))])
            ], [
                IfStatement(
                    BinaryOp(Identifier("x"), ">", IntLiteral(5)),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                        MethodCall("writeStr", [StringLiteral("yes")])
                    ])),
                    None
                )
            ]))
        ])
    ])
    expected = "yes"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_199():
    """Test sequential variable declarations"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, PrimitiveType("int"), [Variable("x", IntLiteral(1))]),
                VariableDecl(False, PrimitiveType("int"), [Variable("y", IntLiteral(2))]),
                VariableDecl(False, PrimitiveType("int"), [Variable("z", IntLiteral(3))])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        BinaryOp(
                            BinaryOp(Identifier("x"), "+", Identifier("y")),
                            "+",
                            Identifier("z")
                        )
                    ])
                ]))
            ]))
        ])
    ])
    expected = "6"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_200():
    """Test variable shadowing in method"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("int"), "test", [
                Parameter(PrimitiveType("int"), "x")
            ], BlockStatement([
                VariableDecl(False, PrimitiveType("int"), [Variable("y", Identifier("x"))])
            ], [
                ReturnStatement(BinaryOp(Identifier("y"), "+", IntLiteral(10)))
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        PostfixExpression(Identifier("Main"), [
                            MethodCall("test", [IntLiteral(5)])
                        ])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "15"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_201():
    """Test boolean variable in condition"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, PrimitiveType("boolean"), [Variable("flag", BoolLiteral(True))])
            ], [
                IfStatement(
                    Identifier("flag"),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                        MethodCall("writeStr", [StringLiteral("true")])
                    ])),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                        MethodCall("writeStr", [StringLiteral("false")])
                    ]))
                )
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_202():
    """Test complex boolean expression"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [
                        BinaryOp(
                            BinaryOp(IntLiteral(5), ">", IntLiteral(3)),
                            "&&",
                            BinaryOp(IntLiteral(2), "<", IntLiteral(4))
                        )
                    ])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_203():
    """Test short-circuit AND evaluation"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [
                        BinaryOp(
                            BoolLiteral(False),
                            "&&",
                            BinaryOp(IntLiteral(5), ">", IntLiteral(3))
                        )
                    ])
                ]))
            ]))
        ])
    ])
    expected = "false"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_204():
    """Test short-circuit OR evaluation"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [
                        BinaryOp(
                            BoolLiteral(True),
                            "||",
                            BinaryOp(IntLiteral(5), "<", IntLiteral(3))
                        )
                    ])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_205():
    """Test float comparison"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [
                        BinaryOp(FloatLiteral(3.14), ">", FloatLiteral(2.5))
                    ])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_206():
    """Test float equality"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [
                        BinaryOp(FloatLiteral(2.5), "==", FloatLiteral(2.5))
                    ])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_207():
    """Test multiple assignments"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, PrimitiveType("int"), [Variable("x", IntLiteral(1))]),
                VariableDecl(False, PrimitiveType("int"), [Variable("y", IntLiteral(2))])
            ], [
                AssignmentStatement(IdLHS("x"), IntLiteral(10)),
                AssignmentStatement(IdLHS("y"), IntLiteral(20)),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [BinaryOp(Identifier("x"), "+", Identifier("y"))])
                ]))
            ]))
        ])
    ])
    expected = "30"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_208():
    """Test assignment with expression"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, PrimitiveType("int"), [Variable("x", IntLiteral(5))])
            ], [
                AssignmentStatement(IdLHS("x"), BinaryOp(Identifier("x"), "*", IntLiteral(2))),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [Identifier("x")])
                ]))
            ]))
        ])
    ])
    expected = "10"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_209():
    """Test method call as expression"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("int"), "getValue", [], BlockStatement([], [
                ReturnStatement(IntLiteral(42))
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, PrimitiveType("int"), [
                    Variable("x", PostfixExpression(Identifier("Main"), [MethodCall("getValue", [])]))
                ])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [Identifier("x")])
                ]))
            ]))
        ])
    ])
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_210():
    """Test nested method calls"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("int"), "double", [
                Parameter(PrimitiveType("int"), "x")
            ], BlockStatement([], [
                ReturnStatement(BinaryOp(Identifier("x"), "*", IntLiteral(2)))
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        PostfixExpression(Identifier("Main"), [
                            MethodCall("double", [
                                PostfixExpression(Identifier("Main"), [
                                    MethodCall("double", [IntLiteral(5)])
                                ])
                            ])
                        ])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "20"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_211():
    """Test simple class with instance attribute"""
    ast = Program([
        ClassDecl("Point", None, [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("x", None)]),
            ConstructorDecl("Point", [
                Parameter(PrimitiveType("int"), "px")
            ], BlockStatement([], [
                AssignmentStatement(
                    PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("x")])),
                    Identifier("px")
                )
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("Point"), [
                    Variable("p", ObjectCreation("Point", [IntLiteral(10)]))
                ])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        PostfixExpression(Identifier("p"), [MemberAccess("x")])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "10"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_212():
    """Test object with multiple attributes"""
    ast = Program([
        ClassDecl("Person", None, [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("age", None)]),
            AttributeDecl(False, False, PrimitiveType("string"), [Attribute("name", None)]),
            ConstructorDecl("Person", [
                Parameter(PrimitiveType("int"), "a"),
                Parameter(PrimitiveType("string"), "n")
            ], BlockStatement([], [
                AssignmentStatement(
                    PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("age")])),
                    Identifier("a")
                ),
                AssignmentStatement(
                    PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("name")])),
                    Identifier("n")
                )
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("Person"), [
                    Variable("p", ObjectCreation("Person", [IntLiteral(25), StringLiteral("John")]))
                ])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeStr", [
                        PostfixExpression(Identifier("p"), [MemberAccess("name")])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "John"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_213():
    """Test object attribute modification"""
    ast = Program([
        ClassDecl("Counter", None, [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("count", None)]),
            ConstructorDecl("Counter", [], BlockStatement([], [
                AssignmentStatement(
                    PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("count")])),
                    IntLiteral(0)
                )
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("Counter"), [
                    Variable("c", ObjectCreation("Counter", []))
                ])
            ], [
                AssignmentStatement(
                    PostfixLHS(PostfixExpression(Identifier("c"), [MemberAccess("count")])),
                    IntLiteral(5)
                ),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        PostfixExpression(Identifier("c"), [MemberAccess("count")])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_214():
    """Test instance method call"""
    ast = Program([
        ClassDecl("Calculator", None, [
            ConstructorDecl("Calculator", [], BlockStatement([], [])),
            MethodDecl(False, PrimitiveType("int"), "add", [
                Parameter(PrimitiveType("int"), "a"),
                Parameter(PrimitiveType("int"), "b")
            ], BlockStatement([], [
                ReturnStatement(BinaryOp(Identifier("a"), "+", Identifier("b")))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("Calculator"), [
                    Variable("calc", ObjectCreation("Calculator", []))
                ])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        PostfixExpression(Identifier("calc"), [
                            MethodCall("add", [IntLiteral(10), IntLiteral(20)])
                        ])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "30"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_215():
    """Test instance method accessing this"""
    ast = Program([
        ClassDecl("Box", None, [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("value", None)]),
            ConstructorDecl("Box", [
                Parameter(PrimitiveType("int"), "v")
            ], BlockStatement([], [
                AssignmentStatement(
                    PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("value")])),
                    Identifier("v")
                )
            ])),
            MethodDecl(False, PrimitiveType("int"), "getValue", [], BlockStatement([], [
                ReturnStatement(PostfixExpression(ThisExpression(), [MemberAccess("value")]))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("Box"), [
                    Variable("box", ObjectCreation("Box", [IntLiteral(99)]))
                ])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        PostfixExpression(Identifier("box"), [MethodCall("getValue", [])])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "99"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_218():
    """Test parenthesized expression"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        BinaryOp(
                            ParenthesizedExpression(BinaryOp(IntLiteral(2), "+", IntLiteral(3))),
                            "*",
                            IntLiteral(4)
                        )
                    ])
                ]))
            ]))
        ])
    ])
    expected = "20"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_219():
    """Test nested parenthesized expressions"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        ParenthesizedExpression(
                            BinaryOp(
                                ParenthesizedExpression(BinaryOp(IntLiteral(1), "+", IntLiteral(2))),
                                "*",
                                ParenthesizedExpression(BinaryOp(IntLiteral(3), "+", IntLiteral(4)))
                            )
                        )
                    ])
                ]))
            ]))
        ])
    ])
    expected = "21"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_220():
    """Test complex nested structures"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, PrimitiveType("int"), [Variable("i", None)])
            ], [
                ForStatement("i", IntLiteral(1), "to", IntLiteral(3),
                    IfStatement(
                        BinaryOp(
                            BinaryOp(Identifier("i"), "%", IntLiteral(2)),
                            "==",
                            IntLiteral(1)
                        ),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeInt", [Identifier("i")])
                        ])),
                        None
                    )
                )
            ]))
        ])
    ])
    expected = "13"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_221():
    """Test variable declared in block"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, PrimitiveType("int"), [Variable("x", IntLiteral(10))])
            ], [
                BlockStatement([
                    VariableDecl(False, PrimitiveType("int"), [Variable("y", IntLiteral(20))])
                ], [
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                        MethodCall("writeInt", [BinaryOp(Identifier("x"), "+", Identifier("y"))])
                    ]))
                ])
            ]))
        ])
    ])
    expected = "30"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_222():
    """Test multiple statements in for loop body"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, PrimitiveType("int"), [Variable("i", None)]),
                VariableDecl(False, PrimitiveType("int"), [Variable("sum", IntLiteral(0))])
            ], [
                ForStatement("i", IntLiteral(1), "to", IntLiteral(3),
                    BlockStatement([], [
                        AssignmentStatement(
                            IdLHS("sum"),
                            BinaryOp(Identifier("sum"), "+", Identifier("i"))
                        ),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                            MethodCall("writeInt", [Identifier("sum")])
                        ]))
                    ])
                )
            ]))
        ])
    ])
    expected = "136"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_223():
    """Test method returning boolean"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("boolean"), "isPositive", [
                Parameter(PrimitiveType("int"), "x")
            ], BlockStatement([], [
                ReturnStatement(BinaryOp(Identifier("x"), ">", IntLiteral(0)))
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [
                        PostfixExpression(Identifier("Main"), [
                            MethodCall("isPositive", [IntLiteral(5)])
                        ])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_224():
    """Test method returning float"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("float"), "average", [
                Parameter(PrimitiveType("float"), "a"),
                Parameter(PrimitiveType("float"), "b")
            ], BlockStatement([], [
                ReturnStatement(
                    BinaryOp(
                        BinaryOp(Identifier("a"), "+", Identifier("b")),
                        "/",
                        FloatLiteral(2.0)
                    )
                )
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeFloat", [
                        PostfixExpression(Identifier("Main"), [
                            MethodCall("average", [FloatLiteral(3.0), FloatLiteral(7.0)])
                        ])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "5.0"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_225():
    """Test method returning string"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("string"), "greet", [
                Parameter(PrimitiveType("string"), "name")
            ], BlockStatement([], [
                ReturnStatement(
                    BinaryOp(StringLiteral("Hello "), "^", Identifier("name"))
                )
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeStr", [
                        PostfixExpression(Identifier("Main"), [
                            MethodCall("greet", [StringLiteral("World")])
                        ])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "Hello World"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_226():
    """Test early return in method"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("int"), "test", [
                Parameter(PrimitiveType("int"), "x")
            ], BlockStatement([], [
                IfStatement(
                    BinaryOp(Identifier("x"), "<", IntLiteral(0)),
                    ReturnStatement(IntLiteral(0)),
                    None
                ),
                ReturnStatement(Identifier("x"))
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        PostfixExpression(Identifier("Main"), [
                            MethodCall("test", [IntLiteral(-5)])
                        ])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "0"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_227():
    """Test multiple return paths"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("string"), "classify", [
                Parameter(PrimitiveType("int"), "x")
            ], BlockStatement([], [
                IfStatement(
                    BinaryOp(Identifier("x"), "<", IntLiteral(0)),
                    ReturnStatement(StringLiteral("negative")),
                    IfStatement(
                        BinaryOp(Identifier("x"), "==", IntLiteral(0)),
                        ReturnStatement(StringLiteral("zero")),
                        ReturnStatement(StringLiteral("positive"))
                    )
                )
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeStr", [
                        PostfixExpression(Identifier("Main"), [
                            MethodCall("classify", [IntLiteral(5)])
                        ])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "positive"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_230():
    """Constructor with no params sets default"""
    ast = Program([
        ClassDecl("Flag", None, [
            AttributeDecl(False, False, PrimitiveType("boolean"), [Attribute("ok", None)]),
            ConstructorDecl("Flag", [], BlockStatement([], [
                AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("ok")])), BoolLiteral(True))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("Flag"), [Variable("f", ObjectCreation("Flag", []))])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [PostfixExpression(Identifier("f"), [MemberAccess("ok")])])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_231():
    """Constructor computes field from param"""
    ast = Program([
        ClassDecl("Square", None, [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("area", None)]),
            ConstructorDecl("Square", [Parameter(PrimitiveType("int"), "side")], BlockStatement([], [
                AssignmentStatement(
                    PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("area")])),
                    BinaryOp(Identifier("side"), "*", Identifier("side"))
                )
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("Square"), [Variable("s", ObjectCreation("Square", [IntLiteral(4)]))])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [PostfixExpression(Identifier("s"), [MemberAccess("area")])])
                ]))
            ]))
        ])
    ])
    expected = "16"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_232():
    """Constructor with string param"""
    ast = Program([
        ClassDecl("Greeter", None, [
            AttributeDecl(False, False, PrimitiveType("string"), [Attribute("msg", None)]),
            ConstructorDecl("Greeter", [Parameter(PrimitiveType("string"), "m")], BlockStatement([], [
                AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("msg")])), Identifier("m"))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("Greeter"), [Variable("g", ObjectCreation("Greeter", [StringLiteral("hi")]))])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeStr", [PostfixExpression(Identifier("g"), [MemberAccess("msg")])])
                ]))
            ]))
        ])
    ])
    expected = "hi"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_233():
    """Destructor present but ignored"""
    ast = Program([
        ClassDecl("Temp", None, [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("x", IntLiteral(1))]),
            ConstructorDecl("Temp", [], BlockStatement([], [])),
            DestructorDecl("~Temp", BlockStatement([], []))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [IntLiteral(9)])
                ]))
            ]))
        ])
    ])
    expected = "9"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_234():
    """Constructor plus destructor in class"""
    ast = Program([
        ClassDecl("Holder", None, [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("v", None)]),
            ConstructorDecl("Holder", [Parameter(PrimitiveType("int"), "v")], BlockStatement([], [
                AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("v")])), Identifier("v"))
            ])),
            DestructorDecl("~Holder", BlockStatement([], []))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("Holder"), [Variable("h", ObjectCreation("Holder", [IntLiteral(12)]))])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [PostfixExpression(Identifier("h"), [MemberAccess("v")])])
                ]))
            ]))
        ])
    ])
    expected = "12"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_235():
    """Inheritance with method override (string)"""
    ast = Program([
        ClassDecl("Animal", None, [
            MethodDecl(False, PrimitiveType("string"), "speak", [], BlockStatement([], [
                ReturnStatement(StringLiteral("animal"))
            ]))
        ]),
        ClassDecl("Dog", "Animal", [
            MethodDecl(False, PrimitiveType("string"), "speak", [], BlockStatement([], [
                ReturnStatement(StringLiteral("dog"))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("Animal"), [Variable("a", ObjectCreation("Dog", []))])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeStr", [
                        PostfixExpression(Identifier("a"), [MethodCall("speak", [])])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "dog"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_236():
    """Inheritance override (int)"""
    ast = Program([
        ClassDecl("Base", None, [
            MethodDecl(False, PrimitiveType("int"), "value", [], BlockStatement([], [
                ReturnStatement(IntLiteral(1))
            ]))
        ]),
        ClassDecl("Derived", "Base", [
            MethodDecl(False, PrimitiveType("int"), "value", [], BlockStatement([], [
                ReturnStatement(IntLiteral(5))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("Base"), [Variable("b", ObjectCreation("Derived", []))])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        PostfixExpression(Identifier("b"), [MethodCall("value", [])])
                    ])
                ]))
            ]))
        ])
    ])
    expected = "5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_237():
    """Polymorphism across two subclasses"""
    ast = Program([
        ClassDecl("Shape", None, [
            MethodDecl(False, PrimitiveType("string"), "kind", [], BlockStatement([], [
                ReturnStatement(StringLiteral("shape"))
            ]))
        ]),
        ClassDecl("Circle", "Shape", [
            MethodDecl(False, PrimitiveType("string"), "kind", [], BlockStatement([], [
                ReturnStatement(StringLiteral("circle"))
            ]))
        ]),
        ClassDecl("Square", "Shape", [
            MethodDecl(False, PrimitiveType("string"), "kind", [], BlockStatement([], [
                ReturnStatement(StringLiteral("square"))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("Shape"), [Variable("s1", ObjectCreation("Circle", []))]),
                VariableDecl(False, ClassType("Shape"), [Variable("s2", ObjectCreation("Square", []))])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeStr", [PostfixExpression(Identifier("s1"), [MethodCall("kind", [])])])
                ])),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeStr", [PostfixExpression(Identifier("s2"), [MethodCall("kind", [])])])
                ]))
            ]))
        ])
    ])
    expected = "circlesquare"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_238():
    """Base reference to derived method chain"""
    ast = Program([
        ClassDecl("Animal", None, [
            MethodDecl(False, PrimitiveType("int"), "age", [], BlockStatement([], [
                ReturnStatement(IntLiteral(1))
            ]))
        ]),
        ClassDecl("Cat", "Animal", [
            MethodDecl(False, PrimitiveType("int"), "age", [], BlockStatement([], [
                ReturnStatement(IntLiteral(3))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("Animal"), [Variable("a", ObjectCreation("Cat", []))])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [PostfixExpression(Identifier("a"), [MethodCall("age", [])])])
                ]))
            ]))
        ])
    ])
    expected = "3"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_239():
    """Polymorphic sequence of calls"""
    ast = Program([
        ClassDecl("Vehicle", None, [
            MethodDecl(False, PrimitiveType("string"), "type", [], BlockStatement([], [
                ReturnStatement(StringLiteral("vehicle"))
            ]))
        ]),
        ClassDecl("Car", "Vehicle", [
            MethodDecl(False, PrimitiveType("string"), "type", [], BlockStatement([], [
                ReturnStatement(StringLiteral("car"))
            ]))
        ]),
        ClassDecl("Bike", "Vehicle", [
            MethodDecl(False, PrimitiveType("string"), "type", [], BlockStatement([], [
                ReturnStatement(StringLiteral("bike"))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("Vehicle"), [Variable("v1", ObjectCreation("Car", []))]),
                VariableDecl(False, ClassType("Vehicle"), [Variable("v2", ObjectCreation("Bike", []))])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeStr", [PostfixExpression(Identifier("v1"), [MethodCall("type", [])])])
                ])),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeStr", [PostfixExpression(Identifier("v2"), [MethodCall("type", [])])])
                ]))
            ]))
        ])
    ])
    expected = "carbike"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_240():
    """Subclass adds new method while overriding existing"""
    ast = Program([
        ClassDecl("Base", None, [
            MethodDecl(False, PrimitiveType("string"), "name", [], BlockStatement([], [
                ReturnStatement(StringLiteral("base"))
            ]))
        ]),
        ClassDecl("Advanced", "Base", [
            MethodDecl(False, PrimitiveType("string"), "name", [], BlockStatement([], [
                ReturnStatement(StringLiteral("adv"))
            ])),
            MethodDecl(False, PrimitiveType("string"), "extra", [], BlockStatement([], [
                ReturnStatement(StringLiteral("plus"))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("Base"), [Variable("b", ObjectCreation("Advanced", []))])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeStr", [PostfixExpression(Identifier("b"), [MethodCall("name", [])])])
                ])),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeStr", [PostfixExpression(Identifier("b"), [MethodCall("extra", [])])])
                ]))
            ]))
        ])
    ])
    expected = "advplus"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_241():
    """Constructor in subclass with override method"""
    ast = Program([
        ClassDecl("Animal", None, [
            AttributeDecl(False, False, PrimitiveType("string"), [Attribute("name", None)]),
            ConstructorDecl("Animal", [Parameter(PrimitiveType("string"), "n")], BlockStatement([], [
                AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("name")])), Identifier("n"))
            ])),
            MethodDecl(False, PrimitiveType("string"), "speak", [], BlockStatement([], [
                ReturnStatement(StringLiteral("?"))
            ]))
        ]),
        ClassDecl("Dog", "Animal", [
            ConstructorDecl("Dog", [Parameter(PrimitiveType("string"), "n")], BlockStatement([], [
                AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("name")])), Identifier("n"))
            ])),
            MethodDecl(False, PrimitiveType("string"), "speak", [], BlockStatement([], [
                ReturnStatement(StringLiteral("woof"))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("Animal"), [Variable("a", ObjectCreation("Dog", [StringLiteral("rex")]))])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeStr", [PostfixExpression(Identifier("a"), [MethodCall("speak", [])])])
                ]))
            ]))
        ])
    ])
    expected = "woof"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_242():
    """Base typed variable holds subclass with overridden method returning int"""
    ast = Program([
        ClassDecl("Counter", None, [
            MethodDecl(False, PrimitiveType("int"), "next", [], BlockStatement([], [
                ReturnStatement(IntLiteral(1))
            ]))
        ]),
        ClassDecl("FastCounter", "Counter", [
            MethodDecl(False, PrimitiveType("int"), "next", [], BlockStatement([], [
                ReturnStatement(IntLiteral(10))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("Counter"), [Variable("c", ObjectCreation("FastCounter", []))])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [PostfixExpression(Identifier("c"), [MethodCall("next", [])])])
                ]))
            ]))
        ])
    ])
    expected = "10"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_243():
    """Inheritance chain depth"""
    ast = Program([
        ClassDecl("A", None, [
            MethodDecl(False, PrimitiveType("string"), "id", [], BlockStatement([], [
                ReturnStatement(StringLiteral("A"))
            ]))
        ]),
        ClassDecl("B", "A", [
            MethodDecl(False, PrimitiveType("string"), "id", [], BlockStatement([], [
                ReturnStatement(StringLiteral("B"))
            ]))
        ]),
        ClassDecl("C", "B", [
            MethodDecl(False, PrimitiveType("string"), "id", [], BlockStatement([], [
                ReturnStatement(StringLiteral("C"))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("A"), [Variable("x", ObjectCreation("C", []))])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeStr", [PostfixExpression(Identifier("x"), [MethodCall("id", [])])])
                ]))
            ]))
        ])
    ])
    expected = "C"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_244():
    """Constructor in base and subclass both set fields"""
    ast = Program([
        ClassDecl("Base", None, [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("x", None)]),
            ConstructorDecl("Base", [Parameter(PrimitiveType("int"), "v")], BlockStatement([], [
                AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("x")])), Identifier("v"))
            ])),
            MethodDecl(False, PrimitiveType("int"), "getX", [], BlockStatement([], [ReturnStatement(PostfixExpression(ThisExpression(), [MemberAccess("x")]))]))
        ]),
        ClassDecl("Sub", "Base", [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("y", None)]),
            ConstructorDecl("Sub", [Parameter(PrimitiveType("int"), "v")], BlockStatement([], [
                AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("x")])), Identifier("v")),
                AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("y")])), BinaryOp(Identifier("v"), "+", IntLiteral(1)))
            ])),
            MethodDecl(False, PrimitiveType("int"), "getY", [], BlockStatement([], [ReturnStatement(PostfixExpression(ThisExpression(), [MemberAccess("y")]))]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("Sub"), [Variable("s", ObjectCreation("Sub", [IntLiteral(4)]))])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [PostfixExpression(Identifier("s"), [MethodCall("getX", [])])])
                ])),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [PostfixExpression(Identifier("s"), [MethodCall("getY", [])])])
                ]))
            ]))
        ])
    ])
    expected = "45"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_245():
    """Override method returning bool"""
    ast = Program([
        ClassDecl("Sensor", None, [
            MethodDecl(False, PrimitiveType("boolean"), "active", [], BlockStatement([], [
                ReturnStatement(BoolLiteral(False))
            ]))
        ]),
        ClassDecl("MockSensor", "Sensor", [
            MethodDecl(False, PrimitiveType("boolean"), "active", [], BlockStatement([], [
                ReturnStatement(BoolLiteral(True))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("Sensor"), [Variable("s", ObjectCreation("MockSensor", []))])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeBool", [PostfixExpression(Identifier("s"), [MethodCall("active", [])])])
                ]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_246():
    """Multiple constructor parameters in inheritance"""
    ast = Program([
        ClassDecl("Base", None, [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("x", None)]),
            ConstructorDecl("Base", [Parameter(PrimitiveType("int"), "a")], BlockStatement([], [
                AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("x")])), Identifier("a"))
            ]))
        ]),
        ClassDecl("Sub", "Base", [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("y", None)]),
            ConstructorDecl("Sub", [
                Parameter(PrimitiveType("int"), "a"),
                Parameter(PrimitiveType("int"), "b")
            ], BlockStatement([], [
                AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("x")])), Identifier("a")),
                AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("y")])), Identifier("b"))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("Sub"), [Variable("s", ObjectCreation("Sub", [IntLiteral(3), IntLiteral(4)]))])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [PostfixExpression(Identifier("s"), [MemberAccess("x")])])
                ])),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [PostfixExpression(Identifier("s"), [MemberAccess("y")])])
                ]))
            ]))
        ])
    ])
    expected = "34"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_247():
    """Polymorphic calls mixed with literals"""
    ast = Program([
        ClassDecl("Printer", None, [
            MethodDecl(False, PrimitiveType("string"), "id", [], BlockStatement([], [ReturnStatement(StringLiteral("P"))]))
        ]),
        ClassDecl("ColorPrinter", "Printer", [
            MethodDecl(False, PrimitiveType("string"), "id", [], BlockStatement([], [ReturnStatement(StringLiteral("C"))]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("Printer"), [Variable("p", ObjectCreation("ColorPrinter", []))])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeStr", [StringLiteral("start")])
                ])),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeStr", [PostfixExpression(Identifier("p"), [MethodCall("id", [])])])
                ])),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeStr", [StringLiteral("end")])
                ]))
            ]))
        ])
    ])
    expected = "startCend"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_228():
    """Constructor sets single field"""
    ast = Program([
        ClassDecl("Point", None, [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("x", None)]),
            ConstructorDecl("Point", [Parameter(PrimitiveType("int"), "a")], BlockStatement([], [
                AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("x")])), Identifier("a"))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("Point"), [Variable("p", ObjectCreation("Point", [IntLiteral(7)]))])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [PostfixExpression(Identifier("p"), [MemberAccess("x")])])
                ]))
            ]))
        ])
    ])
    expected = "7"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_229():
    """Constructor sets multiple fields"""
    ast = Program([
        ClassDecl("Pair", None, [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("a", None), Attribute("b", None)]),
            ConstructorDecl("Pair", [
                Parameter(PrimitiveType("int"), "x"),
                Parameter(PrimitiveType("int"), "y")
            ], BlockStatement([], [
                AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("a")])), Identifier("x")),
                AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("b")])), Identifier("y"))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([
                VariableDecl(False, ClassType("Pair"), [Variable("p", ObjectCreation("Pair", [IntLiteral(2), IntLiteral(5)]))])
            ], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeInt", [
                        BinaryOp(
                            PostfixExpression(Identifier("p"), [MemberAccess("a")]),
                            "+",
                            PostfixExpression(Identifier("p"), [MemberAccess("b")])
                        )
                    ])
                ]))
            ]))
        ])
    ])
    expected = "7"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected



.source Main.java
.class public Main
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
Label0:
	sipush 1000
	bipush 10
	idiv
	invokestatic java/lang/String/valueOf(I)Ljava/lang/String;
	invokestatic io/writeStr(Ljava/lang/String;)V
	return
Label1:
.limit stack 2
.limit locals 1
.end method

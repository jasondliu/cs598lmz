from types import FunctionType
list(FunctionType(lambda x: x + 1, globals(), "func")(1))

# [1, 2]

# 可以看到，FunctionType()的第一个参数是一个code对象，第二个参数是一个dict对象，第三个参数是函数名字符串。
#
# 另外一个类似的函数是types.CodeType，它的参数和FunctionType一样，但是它返回的是code对象。
#
# 这里的code对象就是Python源代码经过编译后的字节码，它的属性有：
#
# co_argcount:

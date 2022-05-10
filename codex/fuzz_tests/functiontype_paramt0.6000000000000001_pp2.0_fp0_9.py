from types import FunctionType
list(FunctionType(list.__code__, globals(), "list"))
# [<built-in function list>]


# 如果这个函数的__code__属性是另一个函数的__code__属性，那么它们的__globals__属性必须相同:
def f():
    ...

def g():
    ...

FunctionType(g.__code__, f.__globals__, "f")
# <function f at 0x7f8a8d8d0400>

FunctionType(g.__code__, g.__globals__, "f")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: __new__() takes 3 positional arguments but 4 were given


# 如果函数的__globals__属性是一个局部

from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['x', 'y']

# 使用函数的__code__属性获取函数的字节码
def func(x, y):
    return x + y

func.__code__

# <code object func at 0x7f8c7d8d3b70, file "<stdin>", line 1>

# 使用函数的__code__属性获取函数的字节码
def func(x, y):
    return x + y

func.__code__.co_code

# b'd\x01\x00S\x00'

# 使用函数的__code__属性获取函数的字节码
def func(x, y):
    return x + y

func.__code__.co

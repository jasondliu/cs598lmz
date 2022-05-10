from types import FunctionType
list(FunctionType(lambda: None).__code__.co_varnames)

# 获取函数的参数注解
from types import FunctionType
def add(a: int, b: int) -> int:
    return a + b
list(FunctionType(add.__code__).__annotations__.items())


# 获取函数的注释
from types import FunctionType
def add(a: int, b: int) -> int:
    '''add two int number'''
    return a + b
FunctionType(add.__code__).__doc__


# 获取函数的作用域
from types import FunctionType
def add(a: int, b: int) -> int:
    return a + b
FunctionType(add.__code__).__globals__

# 获取函数的默认参数
from types import FunctionType
def add(a: int = 0, b: int = 0)

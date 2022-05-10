from types import FunctionType
list(FunctionType(lambda: None, globals()).__code__.co_varnames)

# 使用inspect模块
import inspect
inspect.getargspec(lambda: None)

# 使用函数的__code__属性
def func(a, b, c):
    pass

func.__code__.co_varnames

# 使用函数的__defaults__属性
def func(a, b, c=1, d=2):
    pass

func.__defaults__

# 使用函数的__kwdefaults__属性
def func(a, b, c=1, d=2, *, e, f=3):
    pass

func.__kwdefaults__

# 使用函数的__annotations__属性
def func(a: 1, b: 2, c: 3=1, d: 4=2, *, e: 5, f: 6=

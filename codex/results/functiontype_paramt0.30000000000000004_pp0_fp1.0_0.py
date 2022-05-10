from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# 从一个函数中获取其代码对象
def f():
    pass
f.__code__

# 创建一个新的函数对象
def f():
    pass
def g():
    pass
f.__code__ = g.__code__
f()

# 创建一个新的函数对象
def f():
    pass
def g():
    pass
f.__code__ = g.__code__
f()

# 创建一个新的函数对象
def f():
    pass
def g():
    pass
f.__code__ = g.__code__
f()

# 创建一个新的函数对象
def f():
    pass
def g():
   

from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# 使用函数的__globals__属性
def func():
    pass

func.__globals__

# 使用inspect模块的getmembers()函数
import inspect
inspect.getmembers(func)

# 使用inspect模块的getmodule()函数
inspect.getmodule(func)

# 使用inspect模块的getclosurevars()函数
def func():
    a = 1
    b = 2
    c = 3
    return a + b + c

inspect.getclosurevars(func)

# 使用inspect模块的getclosurevars()函数
def func():
    a = 1
    b = 2
    c = 3
    return a + b + c

inspect.getclosurevars(func)

# 使用inspect

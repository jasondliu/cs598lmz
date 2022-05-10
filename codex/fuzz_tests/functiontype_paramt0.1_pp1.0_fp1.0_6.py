from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# 使用函数类型创建函数
def f(x):
    return x

f1 = FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__)
f1(1)

# 使用函数类型创建函数
def f(x):
    return x

f1 = FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__)
f1(1)

# 使用函数类型创建函数
def f(x):
    return x

f1 = FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__)

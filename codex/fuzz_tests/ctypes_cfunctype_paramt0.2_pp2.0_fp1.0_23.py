import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def func(x):
    return x*x

f = FUNTYPE(func)
print f(2)

# 将函数转换为可调用对象
def func(x):
    return x*x

f = FUNTYPE(func)
print f(2)

# 将函数转换为可调用对象
def func(x):
    return x*x

f = FUNTYPE(func)
print f(2)

# 将函数转换为可调用对象
def func(x):
    return x*x

f = FUNTYPE(func)
print f(2)

# 将函数转换为可调用对象
def func(x):
    return x*x


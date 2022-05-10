import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(x):
    return x + 1

f = FUNTYPE(func)
print(f(1))

# 将函数转换为可调用对象
from ctypes import CFUNCTYPE, c_int

def func(x):
    return x + 1

f = CFUNCTYPE(c_int)(func)
print(f(1))

# 将函数转换为可调用对象
from ctypes import CFUNCTYPE, c_int

def func(x):
    return x + 1

f = CFUNCTYPE(c_int, c_int)(func)
print(f(1))

# 将函数转换为可调用对象
from ctypes import CFUNCTYPE, c_int

def func

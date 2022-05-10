import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(x, y):
    return x + y

f = FUNTYPE(func)
print(f(1, 2))

# 将函数转换为可调用对象
from ctypes import CFUNCTYPE, c_int

def my_sum(x, y):
    return x + y

f = CFUNCTYPE(c_int)(my_sum)
print(f(1, 2))

# 将函数转换为可调用对象
from ctypes import CFUNCTYPE, c_int

def my_sum(x, y):
    return x + y

f = CFUNCTYPE(c_int, c_int, c_int)(my_sum)
print(f(1, 2))

# 将函数转换

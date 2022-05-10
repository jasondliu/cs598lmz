import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    return a + b

f = FUNTYPE(func)
print(f(1, 2))

def func2(a, b):
    return a * b

f = FUNTYPE(func2)
print(f(1, 2))


# 回调函数
from ctypes import *

# 定义回调函数
CMPFUNC = CFUNCTYPE(c_int, c_int, c_int)

def py_cmp_func(a, b):
    print("py_cmp_func", a, b)
    return a - b

cmp_func = CMPFUNC(py_cmp_func)

# 定义一个数组
array = (c_int * 5)(5, 2, 4, 1, 3)

# 调用C库函数
libc = CD

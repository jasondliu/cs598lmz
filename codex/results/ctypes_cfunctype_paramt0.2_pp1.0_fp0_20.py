import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def myfunc(a, b):
    return a + b

myfunc_c = FUNTYPE(myfunc)
print(myfunc_c(1, 2))

# 将函数转换为可调用对象
from ctypes import CFUNCTYPE, c_int

def myfunc(a, b):
    return a + b

myfunc_c = CFUNCTYPE(c_int, c_int, c_int)(myfunc)
print(myfunc_c(1, 2))

# 将函数转换为可调用对象
from ctypes import CFUNCTYPE, c_int

def myfunc(a, b):
    return a + b

myfunc_c = CFUNCTYPE(c_int, c_int, c_int)(myfunc)
print(myfunc

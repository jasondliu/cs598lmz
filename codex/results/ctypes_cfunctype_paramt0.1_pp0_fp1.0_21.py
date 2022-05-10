import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    return a + b

f = FUNTYPE(func)
print(f(1, 2))

# 将函数转换为可调用对象
from ctypes import CFUNCTYPE, c_int

def my_callback(a, b):
    return a + b

CMPFUNC = CFUNCTYPE(c_int, c_int, c_int)

def my_sort(lst, func):
    return sorted(lst, key=func)

lst = [1, 2, 3, 4, 5]
print(my_sort(lst, CMPFUNC(my_callback)))

# 将函数转换为可调用对象
from ctypes import CFUNCTYPE, c_int

def my_callback(a, b):


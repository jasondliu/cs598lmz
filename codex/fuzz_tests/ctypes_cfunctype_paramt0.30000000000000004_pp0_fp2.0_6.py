import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(n):
    return n + 1

func_p = FUNTYPE(func)

print(func_p(3))

# 将c函数转换为python函数
# 使用python内置的ctypes模块，可以将c函数转换为python函数
import ctypes
import sys
from ctypes import c_int, c_char_p, c_void_p

lib = ctypes.CDLL("./libpycall.so")

lib.pycall_init()

# 将c函数转换为python函数
lib.pycall_add.restype = c_int
lib.pycall_add.argtypes = [c_int, c_int]

lib.pycall_print.restype = c_int
lib.pycall_print.arg

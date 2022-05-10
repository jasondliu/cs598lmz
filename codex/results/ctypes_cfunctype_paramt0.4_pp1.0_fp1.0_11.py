import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def f(x, y):
    return x + y

f_cfunc = FUNTYPE(f)
print(f_cfunc(1, 2))

# 将python函数转换为c函数
from ctypes import cdll
libc = cdll.msvcrt

# 将python函数转换为c函数
from ctypes import cdll
libc = cdll.msvcrt

def f(x, y):
    return x + y

f_cfunc = FUNTYPE(f)
libc.printf("%d\n", f_cfunc(1, 2))

# 将python函数转换为c函数
from ctypes import cdll
libc = cdll.msvcrt

def f(x, y):
    return x + y

f_cfunc =

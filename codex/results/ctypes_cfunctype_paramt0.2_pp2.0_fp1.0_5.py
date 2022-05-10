import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    return a + b

f = FUNTYPE(func)
print(f(1, 2))

# 将函数转换为可调用对象
import ctypes

def func(a, b):
    return a + b

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
print(f(1, 2))

# 使用ctypes调用C函数
import ctypes

# 定义C函数
libc = ctypes.CDLL(None)
strcpy = libc.strcpy
strcpy.argtypes = (ctypes.c_char_p, ctypes.c_char_p)
strcpy.restype = ctypes.c_char_p

#

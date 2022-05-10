import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def python_func(n):
    return n + 1
c_func = FUNTYPE(python_func)
print(c_func(2))

# 使用ctypes.CFUNCTYPE创建回调函数
import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int)
def python_func(n):
    print(n * 2)
c_func = FUNTYPE(python_func)
c_func(3)

# 创建一个C函数，接受一个回调函数
import ctypes
def python_func(n):
    return n * 2
c_func = ctypes.CDLL('./c_func.so').c_func
c_func.argtypes = (ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int),)
c_func.rest

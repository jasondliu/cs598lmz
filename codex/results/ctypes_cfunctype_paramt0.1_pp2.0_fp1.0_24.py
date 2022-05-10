import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(x):
    return x + 1

cfunc = FUNTYPE(func)
print(cfunc(1))

# 将函数转换为可调用对象
import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(x):
    return x + 1

cfunc = FUNTYPE(func)
print(cfunc(1))

# 将函数转换为可调用对象
import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(x):
    return x + 1

cfunc = FUNTYPE(func)
print(cfunc(1))

# 将函数转换为可调用

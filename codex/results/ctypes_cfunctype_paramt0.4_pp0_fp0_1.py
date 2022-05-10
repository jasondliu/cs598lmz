import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(n):
    return n + 1

f = FUNTYPE(func)
f(1)

# 2. 使用ctypes模块的动态链接库
import ctypes
lib = ctypes.CDLL('./libfoo.so')
lib.foo(1)

# 3. 使用ctypes模块的动态链接库及回调函数
import ctypes

def func(n):
    return n + 1

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)
lib = ctypes.CDLL('./libfoo.so')
lib.foo(f, 1)

# 4. 使用CFFI模块的动态链接库
import cffi
ffi = cffi.FF

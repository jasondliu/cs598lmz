import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int)

def func(n):
    return n * n

f = FUNTYPE(func)
print f(2)

# 通过ctypes.c_int.in_dll()来访问动态库中的变量

# 通过ctypes.c_int.from_address()来访问内存中的变量

# 通过ctypes.c_int.value来访问变量的值

# 通过ctypes.c_int.value = value来设置变量的值

# 通过ctypes.c_int.__setattr__(value)来设置变量的值

# 通过ctypes.c_int.__getattr__()来访问变量的值


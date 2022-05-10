import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    return a + b

cfunc = FUNTYPE(func)
print(cfunc(1, 2))

# 将函数转换为可调用对象
print(ctypes.cast(cfunc, ctypes.c_void_p).value)

# 将可调用对象转换为函数
print(ctypes.cast(ctypes.c_void_p(id(cfunc)), FUNTYPE)(1, 2))

# 将函数转换为字节串
print(ctypes.string_at(id(cfunc), ctypes.sizeof(cfunc)))

# 将字节串转换为函数
print(ctypes.cast(ctypes.create_string

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def c_add(a, b):
    return a + b

c_add_func = FUNTYPE(c_add)

print(c_add_func(1, 2))

# 将c_add_func转换为ctypes.c_void_p类型
c_add_func_void_p = ctypes.c_void_p(c_add_func)
print(c_add_func_void_p)

# 将c_add_func_void_p转换为ctypes.CFUNCTYPE类型
c_add_func_restore = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int).from_address(c_add_func_void_p)
print(c_add_func_restore(1, 2))

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def c_add(a, b):
    return a + b

c_add_func = FUNTYPE(c_add)

print(c_add_func(1, 2))

# 将函数转换为可调用对象
print(c_add_func)
print(c_add_func(1, 2))

# 将函数转换为可调用对象
print(c_add_func)
print(c_add_func(1, 2))

# 将函数转换为可调用对象
print(c_add_func)
print(c_add_func(1, 2))

# 将函数转换为可调用对象
print

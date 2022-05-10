import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    return a + b

f = FUNTYPE(func)
print(f(1, 2))

# 可以将函数转换为可调用对象
print(f)
print(f(1, 2))

# 可以将函数转换为可调用对象
print(f)
print(f(1, 2))

# 可以将函数转换为可调用对象
print(f)
print(f(1, 2))

# 可以将函数转换为可调用对象
print(f)
print(f(1, 2))

# 可以将函数

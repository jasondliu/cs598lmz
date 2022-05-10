import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    print(a, b)
    return a + b

f = FUNTYPE(func)
f(1, 2)

# 可以把函数转换成可调用对象
print(f)
print(f(1, 2))

# 可以把可调用对象转换成函数
print(f.__call__(1, 2))

# 可以把函数转换成可调用对象
print(FUNTYPE(func))

# 可以把可调用对象转换成函数
print(FUNTYPE(func).__call__(1, 2))

#

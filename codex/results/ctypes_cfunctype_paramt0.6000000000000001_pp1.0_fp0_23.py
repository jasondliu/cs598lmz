import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    return a * b

CMPFUN = FUNTYPE(func)
print(CMPFUN(2, 3))

# 下面的写法也可以
CMPFUN = FUNTYPE(lambda a, b: a * b)
print(CMPFUN(2, 3))

# 如果函数的返回值类型是一个指针，则需要把返回值类型设置为 ctypes.c_void_p
# 返回值是一个字符串
FUNCPTR = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_int)
FUNCPTR(lambda a: str(a))

# 返

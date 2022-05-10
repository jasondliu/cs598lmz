import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def func(a, b):
    return a + b
f = FUNTYPE(func)
f(1, 2)

# 使用ctypes创建函数类型时，它的参数和返回值都必须是ctypes类型，
# 如果不是，需要使用ctypes.c_int来指定。

# 如果需要创建一个函数类型，它的参数是一个指针，可以使用ctypes.POINTER()函数，
# 它接受一个ctypes类型作为参数

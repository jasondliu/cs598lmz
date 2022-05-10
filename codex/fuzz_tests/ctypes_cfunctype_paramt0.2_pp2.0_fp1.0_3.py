import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x*x

f = FUNTYPE(func)
print(f(2))

# 函数指针
# 函数指针是一个指针，它指向一个函数。
# 函数指针可以作为参数传递给另一个函数，这样另一个函数就可以调用它所指向的函数。
# 函数指针可以作为函数的返回值。
# 函数指针可以作为函数的指针数组元素。

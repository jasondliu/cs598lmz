import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def f(x):
    return x*x

f_c = FUNTYPE(f)
print(f_c(3))

# 函数指针
# 函数指针是一种特殊的指针，它指向一个函数。
# 函数指针可以被赋值，可以被调用，可以被比较，可以被传递给函数，可以被函数返回，可以被存储在数组中。
# 函数指针可以被赋值

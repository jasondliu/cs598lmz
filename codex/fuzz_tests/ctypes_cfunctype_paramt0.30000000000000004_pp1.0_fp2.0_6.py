import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(x, y):
    return x + y

f = FUNTYPE(func)
print(f(1, 2))

# 将函数指针传给C
# 如果我们想将函数指针传给C，那么我们需要使用ctypes.addressof()函数，它返回函数的内存地址。
# 我们可以使用ctypes.cast()函数将内存地址转换为函数指针类型。
# 如下所示：

import ctypes

def func(x, y):
    return x + y

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def myfunc(a, b):
    return a + b

f = FUNTYPE(myfunc)
print(f(1, 2))

# 如果一个C函数接受一个函数指针作为参数，那么Python代码就需要使用一个CFUNCTYPE实例来包装目标Python函数。
# 下面是一个例子，它定义了一个C函数，该函数接受一个函数指针作为参数，并调用该函数指针：

import ctypes
lib = ctypes.CDLL

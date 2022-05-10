import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,
                           ctypes.c_int,
                           ctypes.c_int)

def myfunc(a, b):
    return a + b

myfunc_c = FUNTYPE(myfunc)
print(myfunc_c(1, 2))
print(myfunc(1, 2))

# 使用byref()传递指针
# 如果想要传递指针进去，那么就需要使用byref()函数，这个函数可以将一个变量包装为ctypes指针类型。
# 下面是一个例子：

import ctypes

class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
a = fun()  # fun是在python上调用的，而不是在C上调用的，所以a就是一个python的int类型
print(a)

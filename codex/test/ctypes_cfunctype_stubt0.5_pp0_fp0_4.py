import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello World"

a = fun()
print(a)

# 函数指针
print("函数指针")
print(fun)
print(type(fun))
print(fun.__class__)

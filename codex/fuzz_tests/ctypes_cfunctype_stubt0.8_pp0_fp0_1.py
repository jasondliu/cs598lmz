import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello!"

print(fun.__repr__())
print(ctypes.addressof(fun))  # 打印函数的内存地址
print(fun())
print(hex(ctypes.addressof(fun)))  # 打印函数的内存地址

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())

# 可以使用ctypes.cast()函数将一个函数转换为另一种函数类型

# 可以使用ctypes.addressof()函数获取函数的内存地址
print(ctypes.addressof(fun))

# 可以使用ctypes.byref()函数将函数转换为指针类型
print(ctypes.byref(fun))

# 可以使用ctypes.POINTER()函数将函数转换为指针类型

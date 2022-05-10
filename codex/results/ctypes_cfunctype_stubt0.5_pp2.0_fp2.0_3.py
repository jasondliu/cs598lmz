import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print('hello')
    return 1

print(fun())

# 打印函数类型
print(type(fun))

# 打印函数指针
print(ctypes.cast(fun, ctypes.c_void_p).value)

# 打印函数地址
print(hex(id(fun)))

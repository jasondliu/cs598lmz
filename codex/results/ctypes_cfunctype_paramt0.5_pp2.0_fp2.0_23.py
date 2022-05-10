import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
print(FUNTYPE)

# 定义函数类型的参数
def myfunc(a):
    print("myfunc(%s)" % a)
    return 0

ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(myfunc)

# 定义函数类型的参数
def myfunc(a, b):
    print("myfunc(%s,%s)" % (a, b))
    return 0

ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(myfunc)

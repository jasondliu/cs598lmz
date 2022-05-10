import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def myfunc(a, b):
    print(a, b)
    return a + b

myfunc_c = FUNTYPE(myfunc)
print(myfunc_c(2, 3))

# 将函数指针转换为python对象
myfunc_p = ctypes.pythonapi.PyCapsule_New(myfunc_c, None, None)
print(myfunc_p)

# 将python对象转换为函数指针
myfunc_c = ctypes.pythonapi.PyCapsule_GetPointer(myfunc_p, None)
print(myfunc_c(2, 3))

# 将python对象转换为函数指针
myfunc_c = ctypes.pythonapi.PyCapsule_GetPointer

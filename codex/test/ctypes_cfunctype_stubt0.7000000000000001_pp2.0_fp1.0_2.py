import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

print(fun())
print(fun() == 1)
print(type(fun()))

# %%

# 不是所有的c函数都能够被调用，只能调用int float 等其他类型的 c函数会失败
# %%

# 传入参数为int
FUNTYPE2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
@FUNTYPE2
def fun2(a, b):
    return a + b

print(fun2(1, 2))
# %%

# 传入参数为double
FUNTYPE3 = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

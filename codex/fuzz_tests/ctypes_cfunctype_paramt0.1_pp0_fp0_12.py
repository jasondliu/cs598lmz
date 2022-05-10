import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    return a + b

cfunc = FUNTYPE(func)
print(cfunc(1, 2))

# 将cfunc转换为python函数
pfunc = ctypes.pythonapi.PyCFunction_NewEx(cfunc, None, None)
print(pfunc(1, 2))

# 将python函数转换为c函数
cfunc = ctypes.pythonapi.PyCFunction_AsCFunction(pfunc)
print(cfunc(1, 2))

# 将c函数转换为python函数
pfunc = ctypes.pythonapi.PyCFunction_FromCFunction(cfunc, None, None)
print(pfunc(1, 2))

# 将python函数转换为c函数
cfunc = ctypes

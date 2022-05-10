import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(x):
    return x+1

f = FUNTYPE(myfunc)
f(1)

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# restype: 返回值类型
# argtypes: 参数类型
# use_errno: 如果设置为True，则函数返回错误码，而不是返回值
# use_last_error: 如果设置为True，则函数调用会设置Windows的GetLastError()

# 如果函数返回值是void，则restype设置

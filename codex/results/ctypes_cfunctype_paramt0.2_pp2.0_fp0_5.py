import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(x):
    return x*x

f = FUNTYPE(func)
print f(2)

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# restype: 返回值类型
# argtypes: 参数类型
# use_errno: 如果为真，则调用函数后会检查errno
# use_last_error: 如果为真，则调用函数后会检查GetLastError()

# 创建一个函数类型
# 创建一个函数类型，返回值为

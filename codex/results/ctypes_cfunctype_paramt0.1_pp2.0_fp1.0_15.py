import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(x):
    return x + 1

cfunc = FUNTYPE(func)
print(cfunc(1))

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# restype: 返回值类型
# argtypes: 参数类型
# use_errno: 如果设置为True，则函数返回错误码，并将错误码保存在ctypes.get_errno()中
# use_last_error: 如果设置为True，则函数返回错误码，并将错误码保存在ctypes.get_

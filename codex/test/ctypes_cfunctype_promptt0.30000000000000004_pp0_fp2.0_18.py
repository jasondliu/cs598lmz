import ctypes
# Test ctypes.CFUNCTYPE()

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# restype: 返回值类型
# argtypes: 参数类型
# use_errno: 是否使用errno
# use_last_error: 是否使用GetLastError()

# 创建一个函数类型
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def py_cmp_func(a, b):
    print("py_cmp_func", a, b)
    return a - b

# 将python函数转换为C函数
cmp_func = CMPFUNC(py_cmp_func)

# 使用

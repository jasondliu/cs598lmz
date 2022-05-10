import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# restype: 返回值类型
# argtypes: 参数类型
# use_errno: 是否使用errno
# use_last_error: 是否使用GetLastError

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# restype: 返回值类型
# argtypes: 参数类型
# use_errno: 是否使用errno
# use_last_error: 是否使用GetLastError

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)

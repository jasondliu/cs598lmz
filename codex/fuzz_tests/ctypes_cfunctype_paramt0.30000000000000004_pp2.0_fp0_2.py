import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

f_c = FUNTYPE(f)
f_c(2)

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# restype: 返回值类型
# argtypes: 参数类型
# use_errno: 如果为真，则使用errno作为错误号
# use_last_error: 如果为真，则使用GetLastError()作为错误号

# ctypes.c_bool
# ctypes.c_char
# ctypes.c_wchar
# ctypes.c_byte
# ctypes.c_ubyte
# ctypes.c_short
# ctypes.c_ushort
# c

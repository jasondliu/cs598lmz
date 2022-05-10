import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# restype: 返回值类型
# argtypes: 参数类型
# use_errno: 如果为真，则返回错误码，否则返回-1
# use_last_error: 如果为真，则返回错误码，否则返回0
# 可以使用ctypes.c_int来表示int类型
# 可以使用ctypes.c_char_p来表示char*类型
# 可以使用ctypes.c_

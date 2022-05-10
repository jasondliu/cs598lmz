import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun()

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# restype: 返回值类型
# *argtypes: 参数类型
# use_errno: 如果为真，则函数的返回值将被视为错误代码，并且会设置ctypes.get_errno()的值
# use_last_error: 如果为真，则函数的返回值将被视为错误代码，并且会设置ctypes.get_last_error()的值

# 如果函数返

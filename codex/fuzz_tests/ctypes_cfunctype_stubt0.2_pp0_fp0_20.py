import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print fun()

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# restype: 返回值类型
# argtypes: 参数类型
# use_errno: 如果设置为True，则函数返回值为一个元组(result, errno)
# use_last_error: 如果设置为True，则函数返回值为一个元组(result, last_error)

# 函数调用
# 函数调用的返回值是一个元组，元组中包含了函数的返回

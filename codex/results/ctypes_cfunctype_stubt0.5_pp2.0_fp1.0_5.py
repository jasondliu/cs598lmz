import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
fun()

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# restype: 返回类型
# argtypes: 参数类型
# use_errno: 如果函数调用失败，返回错误码
# use_last_error: 如果函数调用失败，返回错误码

# ctypes.create_string_buffer(init, size=None)
# 创建可以修改的字符串
# init: 字符串
# size: 缓冲区大小

# ctypes.create_unicode_buffer(init, size=None)
# 创建

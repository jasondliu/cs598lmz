import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello'

fun()

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# restype: the result type of the function.
# argtypes: a sequence of the argument types of the function.
# use_errno: if true, the function will check for the C variable errno and throw an exception when it is non-zero.
# use_last_error: if true, the function will check for the C variable GetLastError() and throw an exception when it is non-zero.
# 这个函数返回一个基于函数类型的对象，它是一个类，它的实例是一个可调用的C函数对象。
# 所创建的可调用对象的参数类型

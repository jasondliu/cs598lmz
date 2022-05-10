import ctypes
# Test ctypes.CFUNCTYPE
# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# 创建一个C函数原型对象，该对象可用于调用C函数。 参数restype和argtypes由ctypes类型组成，它们描述函数的返回类型和参数类型。
# 如果参数use_errno是真的，则在调用C函数时，将检查errno的值，并在出错时引发WindowsError或OSError。
# 如果参数use_last_error是真的

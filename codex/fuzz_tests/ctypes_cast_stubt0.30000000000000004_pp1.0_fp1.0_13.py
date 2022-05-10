import ctypes
ctypes.cast(0, ctypes.py_object).value

# 或者使用 ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
# ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [ctypes.py_object]
# ctypes.pythonapi.PyCObject_AsVoidPtr(obj)

# 将 C 结构体转换为 Python 对象
# 将 C 结构体转换为 Python 对象的反向过程同样简单。
# 只需使用 ctypes.pythonapi.PyCObject_FromVoidPtr 方法，并将 C 结构体的地址作为参数传入即可。
# 下面是一个示

import ctypes
ctypes.cast(0, ctypes.py_object).value

# 下面的代码会报错，因为ctypes.py_object不能接受一个非对象的指针
#ctypes.cast(id(int), ctypes.py_object).value

# 下面的代码也会报错，因为ctypes.py_object不能接受一个空指针
#ctypes.cast(None, ctypes.py_object).value

# 可以使用ctypes.pythonapi.PyCObject_AsVoidPtr()函数获取对象的指针
ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
ctypes.pythonapi.PyCObject_AsVoidPtr.arg

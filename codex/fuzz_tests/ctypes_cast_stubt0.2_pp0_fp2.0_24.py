import ctypes
ctypes.cast(id(int), ctypes.py_object).value

# 使用ctypes.pythonapi.PyCapsule_GetPointer()方法获取指针
ctypes.pythonapi.PyCapsule_GetPointer.restype = ctypes.c_void_p
ctypes.pythonapi.PyCapsule_GetPointer.argtypes = [ctypes.py_object]
ctypes.pythonapi.PyCapsule_GetPointer(id(int))

# 使用ctypes.pythonapi.PyCObject_AsVoidPtr()方法获取指针
ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [ctypes.py_object]
ctypes.pythonapi.PyCObject_AsVoidPtr(id(int))

# 使用ctypes.pythonapi.PyLong_AsVoidPtr()方

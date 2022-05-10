import ctypes
ctypes.cast(id(int), ctypes.py_object).value

# 使用ctypes.pythonapi.PyCapsule_GetPointer()方法获取指针
ctypes.pythonapi.PyCapsule_GetPointer.restype = ctypes.c_void_p
ctypes.pythonapi.PyCapsule_GetPointer.argtypes = [ctypes.py_object]

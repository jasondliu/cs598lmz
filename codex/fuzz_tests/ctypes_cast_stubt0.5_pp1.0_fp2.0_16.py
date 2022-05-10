import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is equivalent to the above:
ctypes.pythonapi.PyCapsule_GetPointer.restype = ctypes.c_void_p
ctypes.pythonapi.PyCapsule_GetPointer.argtypes = [ctypes.py_object, ctypes.c_char_p]
ctypes.pythonapi.PyCapsule_GetPointer(ctypes.py_object(0), None)

# This is equivalent to the above:
ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [ctypes.py_object]
ctypes.pythonapi.PyCObject_AsVoidPtr(ctypes.py_object(0))

# This is equivalent to the above:
ctypes.pythonapi.PyLong_AsVoidPtr.restype = ctypes.c_void_p
ctypes.pythonapi.PyLong_AsVoidPtr.argtypes = [ct

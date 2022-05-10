import ctypes
ctypes.cast(0, ctypes.py_object)

# This is the same as the above, but it's a little more explicit.
ctypes.pythonapi.PyCapsule_GetPointer.restype = ctypes.c_void_p
ctypes.pythonapi.PyCapsule_GetPointer.argtypes = [ctypes.py_object, ctypes.c_char_p]
ctypes.pythonapi.PyCapsule_GetPointer(0, 0)

# This is the same as the above, but it's a little more explicit.
ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [ctypes.py_object]
ctypes.pythonapi.PyCObject_AsVoidPtr(0)

# This is the same as the above, but it's a little more explicit.
ctypes.pythonapi.PyCapsule_GetPointer.restype = ctypes.c_void_p
ctypes.pythonapi.

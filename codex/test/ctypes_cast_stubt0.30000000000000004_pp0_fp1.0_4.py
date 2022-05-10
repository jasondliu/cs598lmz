import ctypes
ctypes.cast(0, ctypes.py_object)

# This is the same as the above, but it's a little more explicit.
ctypes.pythonapi.PyCapsule_GetPointer.restype = ctypes.c_void_p
ctypes.pythonapi.PyCapsule_GetPointer.argtypes = [ctypes.py_object, ctypes.c_char_p]

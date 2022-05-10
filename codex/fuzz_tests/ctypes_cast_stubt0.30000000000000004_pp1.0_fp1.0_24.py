import ctypes
ctypes.cast(0, ctypes.py_object).value

# this is the same as the above
ctypes.pythonapi.PyCapsule_GetPointer.restype = ctypes.c_void_p
ctypes.pythonapi.PyCapsule_GetPointer.argtypes = [ctypes.py_object, ctypes.c_char_p]
ctypes.pythonapi.PyCapsule_GetPointer(ctypes.py_object(0), None)

# this is the same as the above
ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [ctypes.py_object]
ctypes.pythonapi.PyCObject_AsVoidPtr(ctypes.py_object(0))

# this is the same as the above
ctypes.pythonapi.PyCObject_FromVoidPtr.restype = ctypes.py_object
ctypes.pythonapi.PyCObject_FromVoidPtr.argtypes = [ct

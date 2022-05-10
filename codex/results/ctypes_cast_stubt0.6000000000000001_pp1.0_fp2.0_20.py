import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is the same as:
ctypes.pythonapi.PyCapsule_GetPointer.restype = ctypes.c_void_p
ctypes.pythonapi.PyCapsule_GetPointer(ctypes.py_object(0), None)

# This is the same as:
ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
ctypes.pythonapi.PyCObject_AsVoidPtr(ctypes.py_object(0))
</code>


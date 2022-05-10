import ctypes
ctypes.cast(0, ctypes.py_object).value

# this is the same as the above
ctypes.pythonapi.PyCapsule_GetPointer.restype = ctypes.c_void_p
ctypes.pythonapi.PyCapsule_GetPointer.argtypes = [ctypes.py_object, ctypes.c_char_p]
ctypes.pythonapi.PyCapsule_GetPointer(ctypes.py_object(0), b"PyCapsule_Type").value
</code>


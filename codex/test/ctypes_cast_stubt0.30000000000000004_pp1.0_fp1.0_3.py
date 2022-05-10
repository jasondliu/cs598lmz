import ctypes
ctypes.cast(0, ctypes.py_object)
# ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
# ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [ctypes.py_object]
# ctypes.pythonapi.PyCObject_AsVoidPtr(ctypes.py_object(0))
# ctypes.pythonapi.PyCObject_AsVoidPtr(0)
# ctypes.pythonapi.PyCObject_AsVoidPtr(ctypes.c_void_p(0))

# ctypes.pythonapi.PyCObject_FromVoidPtr.restype = ctypes.py_object
# ctypes.pythonapi.PyCObject_FromVoidPtr.argtypes = [ctypes.c_void_p, ctypes.CFUNCTYPE(None)]
# ctypes.pythonapi.PyCObject_FromVoidPtr(ctypes.c_void_p(0), None)

# ctypes.pythonapi.PyCObject_Import.restype = c

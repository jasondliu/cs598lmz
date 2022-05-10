import ctypes
ctypes.cast(0, ctypes.py_object).value

# ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
# ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [ctypes.py_object]
# ctypes.pythonapi.PyCObject_AsVoidPtr(ctypes.py_object(0))
# ctypes.pythonapi.PyCObject_AsVoidPtr(ctypes.py_object(0))
# segfault

# ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
# ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [ctypes.py_object]
# ctypes.pythonapi.PyCObject_AsVoidPtr(ctypes.py_object(None))
# segfault

# ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
# ctypes.pythonapi.PyCObject_

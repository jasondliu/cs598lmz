import ctypes
# Test ctypes.CFUNCTYPE
i = ctypes.c_int.in_dll(ctypes.pythonapi, 'Py_IsInitialized')


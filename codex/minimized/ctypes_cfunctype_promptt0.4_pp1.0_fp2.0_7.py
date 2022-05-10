import ctypes
c_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(lambda x, y: x + y)
c_func = ctypes.cast(c_func, ctypes.c_void_p).value
c_func = ctypes.pythonapi.PyCapsule_GetPointer(c_func, b"_C_API")

import ctypes
# Test ctypes.CFUNCTYPE()
c_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(lambda x, y: x + y)
print(c_func(1, 2))

# Test ctypes.cast()
c_func = ctypes.cast(c_func, ctypes.c_void_p).value
print(c_func)

# Test ctypes.POINTER()
c_func = ctypes.cast(ctypes.c_void_p(c_func), ctypes.POINTER(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int))).contents
print(c_func(1, 2))

# Test ctypes.pythonapi.PyCapsule_GetPointer()
c_func = ctypes.pythonapi.PyCapsule_GetPointer(c_func, b"_C_API")
print(c_func)

# Test ctypes.pythonapi.PyCapsule_New()
c

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
# Initialize instance using a function pointer of the given type
instance = MyClass(FUNTYPE(my_function))
</code>


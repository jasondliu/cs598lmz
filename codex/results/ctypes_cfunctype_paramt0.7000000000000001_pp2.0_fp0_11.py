import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p)
ptr = ctypes.cast(id(foo), FUNTYPE)
print(ptr())
</code>


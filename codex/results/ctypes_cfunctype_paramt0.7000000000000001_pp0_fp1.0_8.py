import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_long, ctypes.c_int)
funptr = FUNTYPE.in_dll(ctypes.cdll.LoadLibrary("libpyfun.so"), "fun")
print(funptr(1))
</code>


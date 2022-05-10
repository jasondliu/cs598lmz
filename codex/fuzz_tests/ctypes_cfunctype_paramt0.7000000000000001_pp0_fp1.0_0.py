import ctypes
FUNTYPE = ctypes.CFUNCTYPE( ctypes.c_int,  ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int) )

# Allocate the function pointer
p = ctypes.cdll.LoadLibrary("/lib/libc.so.6")
p.syscall.restype = ctypes.c_int
p.syscall.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]

# Call the function.
result = p.syscall(0, 0, 0, 0)
print("result = ", result)
</code>


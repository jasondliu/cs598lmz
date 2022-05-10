import ctypes
# Test ctypes.CFUNCTYPE
print("Test ctypes.CFUNCTYPE")
x = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
print("type(x)", type(x))
print("x", x)
print("x.argtypes", x.argtypes)
print("x.restype", x.restype)
# Test ctypes.PYFUNCTYPE
print("Test ctypes.PYFUNCTYPE")
x = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int)
print("type(x)", type(x))
print("x", x)
print("x.argtypes", x.argtypes)
print("x.restype", x.restype)


# Test ctypes.cast
# Test ctypes.byref
# Test ctypes.POINTER
print("Test ctypes.POINTER")
x = ctypes.POINTER(ctypes.c_int)
print("type(x)", type(x))
print("x", x)
# Test ctypes.pointer

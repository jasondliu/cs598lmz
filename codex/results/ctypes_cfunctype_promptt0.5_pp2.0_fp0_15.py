import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
lib.add.argtypes = (ctypes.c_int, ctypes.c_int)
lib.add.restype = ctypes.c_int
lib.add(1, 2)

# Test ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
lib.add_double.argtypes = (ctypes.c_double, ctypes.c_double)
lib.add_double.restype = ctypes.c_double
lib.add_double(1.1, 2.2)

# Test ctypes.CFUNCTYPE(None, ctypes.c_int)
lib.print_int.argtypes = (ctypes.c_int,)
lib.print_int.restype = None
lib.print_int(3)

# Test ctypes.CFUNCTYPE(None, ctypes.c_double)
lib.print_double.argtypes = (ctypes.c_double,)
lib.print_double.restype = None

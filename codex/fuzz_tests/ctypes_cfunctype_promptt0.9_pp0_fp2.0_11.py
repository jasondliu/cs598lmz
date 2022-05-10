import ctypes
# Test ctypes.CFUNCTYPE compile

ctypes.CFUNCTYPE(None)

# Test ctypes.POINTER(*type) compile
ctypes.POINTER(ctypes.c_int)
ctypes.POINTER(ctypes.c_float)
ctypes.POINTER(ctypes.c_double)
ctypes.POINTER(ctypes.c_char)
# Error - cannot create pointer to pointer
#ctypes.POINTER(ctypes.POINTER(ctypes.c_int))

# Test ctypes.c_int alias
ctypes.c_int
# Test ctypes.c_int(*variable)
fcn_int = ctypes.c_int(5)

# Test ctypes.c_float(*variable)
fcn_float = ctypes.c_float(3.14)

# Test ctypes.c_double(*variable)
fcn_double = ctypes.c_double(3)

# Test ctypes.c_char(*variable)
fcn_char = ctypes.c_char('a')

# Test ctypes.Cast(value,

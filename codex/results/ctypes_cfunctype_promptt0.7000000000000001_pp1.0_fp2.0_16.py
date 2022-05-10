import ctypes
# Test ctypes.CFUNCTYPE(type, ...)
CFUNCTYPE = ctypes.CFUNCTYPE
cdouble = ctypes.c_double
cint = ctypes.c_int
cfloat = ctypes.c_float
cchar = ctypes.c_char
cvoid = ctypes.c_void_p

f = CFUNCTYPE(cint, cdouble, cfloat, cchar, cint, cvoid)
print(f)
assert issubclass(f, CFUNCTYPE)
assert issubclass(f, type(CFUNCTYPE))

# Test ctypes.POINTER(type)
POINTER = ctypes.POINTER
doublep = POINTER(ctypes.c_double)
assert POINTER(ctypes.c_double) is doublep

# Test ctypes.cast(obj, type)
cast = ctypes.cast
p = cast((cint * 3)(1, 2, 3), POINTER(cint))
assert p[0] == 1
assert p[1] == 2
assert p[2] == 3
assert cast(

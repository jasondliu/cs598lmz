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

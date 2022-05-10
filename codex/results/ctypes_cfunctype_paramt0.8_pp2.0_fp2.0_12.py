import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
f = FUNTYPE(lambda x: x*x+1)
print("Calling f(1) returns", f(1))

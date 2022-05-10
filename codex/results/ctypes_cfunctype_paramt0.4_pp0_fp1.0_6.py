import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def make_function(f, argtype=ctypes.c_double, restype=ctypes.c_double):
    return FUNTYPE((argtype,), restype)(f)

def f(x):
    return x**2

f_c = make_function(f)
print(f_c(2))

f_c = make_function(f, ctypes.c_int, ctypes.c_int)
print(f_c(2))

f_c = make_function(f, ctypes.c_int, ctypes.c_float)
print(f_c(2))

f_c = make_function(f, ctypes.c_float, ctypes.c_int)
print(f_c(2))

f_c = make_function(f, ctypes.c_float, ctypes.c_float)
print(f_c(2))

f_c = make_function(f, ctypes.c_double, ctypes.c

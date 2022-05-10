import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

f_c = FUNTYPE(f)

print f_c(2)

# ctypes.c_double(2)

# ctypes.c_double(f(2))

# f_c(ctypes.c_double(2))

# f_c(2)

# f_c(ctypes.c_double(2))

# f_c(ctypes.c_double(2))

# f_c(ctypes.c_double(2))

# f_c(ctypes.c_double(2))

# f_c(ctypes.c_double(2))

# f_c(ctypes.c_double(2))

# f_c(ctypes.c_double(2))

# f_c(ctypes.c_double(2))

# f_c(ctypes.c_double(2))

# f_c(ctypes.c_double

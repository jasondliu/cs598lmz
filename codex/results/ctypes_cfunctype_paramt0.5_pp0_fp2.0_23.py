import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)

# import the shared library into ctypes
lib = ctypes.CDLL('./libintegrate.so')

# map the C functions to Python functions
lib.integrate.restype = ctypes.c_double
lib.integrate.argtypes = [FUNTYPE, ctypes.c_double, ctypes.c_double, ctypes.c_double]

# define a Python function that calls the C function
def integrate(f, a, b, dx):
    return lib.integrate(f, a, b, dx)

# define a C function that returns C_DOUBLE
def f(x,y,z):
    return math.sin(x*y*z)

# define a Python function that calls the C function
f_c = FUNTYPE(f)

# call the C function
print integrate(f_c, 0, 1, 0.001)

# call the C function again
print integrate(f_c, 0, 1

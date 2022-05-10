import ctypes
FUNTYPE = ctypes.CFUNCTYPE(
    ctypes.c_double, # return type
    ctypes.c_double, # arg1
    ctypes.c_double, # arg2
    ctypes.c_void_p, # arg3
)

# A C-function that takes a function pointer as argument.
# The signature of the function pointer must match FUNTYPE.
c_squarer = ctypes.CDLL('./libsquarer.so').squarer
c_squarer.argtypes = (FUNTYPE, ctypes.c_double, ctypes.c_void_p)
c_squarer.restype = ctypes.c_double

# A Python function that matches the signature of FUNTYPE.
def python_squarer(x, y, data):
    return x * y * data

# A ctypes function pointer with the signature of FUNTYPE.
# The Python function is converted to this function pointer.
c_squarer_func = FUNTYPE(python_squarer)

c_squarer(c_squarer_func, 2.0, 4.0, None)
# 16.0
</

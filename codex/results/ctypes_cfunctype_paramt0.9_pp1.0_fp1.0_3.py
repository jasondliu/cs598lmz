import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,
                           ctypes.c_double,
                           c_int)  # from the lib.h file

# load the shared object file
C = ctypes.CDLL('./lib.so')

# initialize it with your C function
C.examplefunc.argtypes = (ctypes.c_double, ctypes.c_int) # set args
C.examplefunc.restype = ctypes.c_double # set return type

c_function = C.examplefunc
# decorate with the actual type
cfunc = FUNTYPE(c_function)
</code>
And you can use it just like Python,
<code>cfunc(3.0, 4)
</code>
which returns <code>3.0</code>, of course.


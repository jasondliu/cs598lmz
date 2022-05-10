import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double)

# Define the callback function.
@FUNTYPE
def callback(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4):
    print x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4
    return 0

# Convert the Python function into a C function.
cfunc = FUNTYPE(callback)

# Load the library.
lib = ctypes.CDLL('libtestlib.so')

# Set the callback.
lib.set_callback(cfunc)

# Call the function that makes the callbacks.
lib.do_callbacks()
</code

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

# Load the binary module
lib = ctypes.CDLL('./lib/libMyModule.dylib')

# Define a wrapper function for the function in the module
@FUNTYPE
def f(x):
    return lib.f(x)

print(f(3.14))
</code>


import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

def add_c_function(lib, name, func):
    cfunc = FUNTYPE(func)
    setattr(lib, name, cfunc)

# The C library
lib = ctypes.cdll.LoadLibrary('./libexample.so')

# Add the C function to the library
add_c_function(lib, 'add', add)

# Call the C function
print(lib.add(1, 2))
</code>


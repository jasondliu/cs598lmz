import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

# Create a C function pointer from the Python function.
# This is a bit delicate, as the ctypes.CFUNCTYPE()
# creates a new C function type, but we want to use
# the exact same type as the cffi function type.  We
# cheat by looking at the _type_ pointer of the cffi
# function.
c_fun = ctypes.cast(ffi.cast("void *", fun), ffi.typeof(f)).value

# Call the C function through the cffi function
print f(c_fun)
</code>


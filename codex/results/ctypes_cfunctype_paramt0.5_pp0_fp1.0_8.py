import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

lib = ctypes.cdll.LoadLibrary("./libfunc.so")
lib.f.restype = ctypes.c_double
lib.f.argtypes = (ctypes.c_double,)

# Call the function
print(lib.f(2.0))

# Get a pointer to the function
f = lib.f

# Call the function using the pointer
print(f(2.0))

# Convert the pointer to a function object
f = FUNTYPE(lib.f)

# Call the function using the function object
print(f(2.0))
</code>


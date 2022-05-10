import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Load the shared library into ctypes.
lib = ctypes.CDLL('./libfoo.so')

# Set the return type of the function 'foo'
lib.foo.restype = ctypes.c_int

# Set the arg types of the function 'foo'
lib.foo.argtypes = [ctypes.c_int, ctypes.c_int]

# Call the function 'foo' directly.
lib.foo(1, 2)

# Call the function 'foo' via the Python wrapper.
foo(1, 2)

# Call the function 'foo' via the ctypes CFUNCTYPE wrapper.
func = FUNTYPE(lib.foo)
func(1, 2)

# Call the function 'foo' via the ctypes CFUNCTYPE wrapper,
# and pass it to a function that takes a function pointer.
bar(func)
</code>


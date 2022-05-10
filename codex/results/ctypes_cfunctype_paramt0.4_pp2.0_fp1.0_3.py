import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# The C function
def my_function(a, b):
    return a + b

# Convert the Python function to a C function
cfunc = FUNTYPE(my_function)

# Call the C function
print(cfunc(1, 2))

# Also call the C function via the Python wrapper
print(my_function(1, 2))

# The C function is still available
print(cfunc)

# But the Python function is gone
#print(my_function)

# The following is a more complex example

# A C function that takes a function as an argument
libc = ctypes.CDLL(None)
cfunc = libc.printf
cfunc.argtypes = [ctypes.c_char_p]
cfunc.restype = ctypes.c_int

# A Python function that takes a function as an argument
def my_function(func):
    func("Hello, World!")

# Convert the Python function to a C function
cfunc =

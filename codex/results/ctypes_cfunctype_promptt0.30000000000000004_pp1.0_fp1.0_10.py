import ctypes
# Test ctypes.CFUNCTYPE

libc = ctypes.CDLL(ctypes.util.find_library('c'))

# prototype a function
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# define the function
def c_function(arg):
    return arg * 5

# convert the function
c_function_type = prototype(c_function)

# call the function
result = libc.abs(c_function_type(-3))

print(result)

# Test ctypes.PYFUNCTYPE

libc = ctypes.CDLL(ctypes.util.find_library('c'))

# prototype a function
prototype = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int)

# define the function
def py_function(arg):
    return arg * 5

# convert the function
py_function_type = prototype(py_function)

# call the function
result = libc.abs(py_function_type(-3))

print

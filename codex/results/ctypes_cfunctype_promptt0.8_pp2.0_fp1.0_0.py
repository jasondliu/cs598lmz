import ctypes
# Test ctypes.CFUNCTYPE

# Using the prototype from libsample.h:
# 
# int print_hello_world(void);

_libsample = cdll.LoadLibrary('./libsample.so')

# Wrap the library function using the prototype.
print_hello_world = _libsample.print_hello_world
print_hello_world.restype = ctypes.c_int

r = print_hello_world()
print(r)

# Test ctypes.Array

_libsample = cdll.LoadLibrary('./libsample.so')

# Create a C Array of c_int.
c_array = ctypes.c_int * 3

# Create a Python 3 tuple of ints.
py_array = (1, 2, 3)

# Convert the Python 3 tuple to a C Array.
c_array = c_array(*py_array)

# Wrap the library function using the prototype.
sum_array = _libsample.sum_array
sum_array.restype = ctypes.c_int
sum_array.argtypes = (c_array,)

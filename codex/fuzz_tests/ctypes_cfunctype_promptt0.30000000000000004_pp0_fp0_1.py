import ctypes
# Test ctypes.CFUNCTYPE

libc = ctypes.CDLL(ctypes.util.find_library("c"))

# Create a CFUNCTYPE for a function that returns an int, and takes
# two ints as arguments.
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Create a function that takes two ints as arguments and returns
# the sum of the two.
@prototype
def int_add(a, b):
    return a + b

# Call the function.
print(int_add(1, 2))

# Call the function using the ctypes.c_int types.
print(int_add(ctypes.c_int(1), ctypes.c_int(2)))

# Call the function using the ctypes.c_int types, but use keyword
# arguments.
print(int_add(a=ctypes.c_int(1), b=ctypes.c_int(2)))

# Call the function using the ctypes.c_int types, but use keyword

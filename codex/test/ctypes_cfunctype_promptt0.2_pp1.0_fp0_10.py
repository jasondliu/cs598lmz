import ctypes
# Test ctypes.CFUNCTYPE()

# This is a function that takes a function pointer as an argument
# and calls it.

# The function pointer should take an int and return an int.

# This is the function we will pass to the test function.
def func(i):
    return i + 1

# This is the function pointer type we will use.

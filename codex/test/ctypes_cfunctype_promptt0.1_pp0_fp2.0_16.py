import ctypes
# Test ctypes.CFUNCTYPE

# This is a test of the ctypes.CFUNCTYPE function.
#
# The test is to create a function pointer to a function that takes
# a single integer argument and returns an integer.  The function
# pointer is then called with a number of different arguments.
#
# The test passes if the function pointer returns the same value as
# the function it points to.

import ctypes

# Create a function pointer to a function that takes an integer
# argument and returns an integer.

func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x)

# Call the function pointer with a number of different arguments.

assert func(0) == 0
assert func(1) == 1
assert func(2) == 2
assert func(3) == 3
assert func(4) == 4
assert func(5) == 5
assert func(6) == 6
assert func(7) == 7
assert func(8) == 8
assert func(9) == 9
assert func(10) == 10
assert func(11)

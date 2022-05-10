import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is used to verify the correct behavior of ctypes.CFUNCTYPE.
#
# The test creates a function pointer to a function that takes a single
# argument and returns the value of the argument.  The test then calls
# the function pointer with a variety of values and checks that the
# return value matches the argument.
#
# The test also creates a function pointer to a function that takes two
# arguments and returns the sum of the arguments.  The test then calls
# the function pointer with a variety of values and checks that the
# return value is the sum of the arguments.
#
# The test also creates a function pointer to a function that takes a
# single argument and returns the value of the argument.  The test then
# passes the function pointer as an argument to a function that returns
# the value of the argument.  The test checks that the return value
# matches the original argument.
#
# The test also creates a function pointer to a function that takes a
# single argument and returns the value of the argument.  The test then
# passes the function pointer as an argument to a function that returns
#

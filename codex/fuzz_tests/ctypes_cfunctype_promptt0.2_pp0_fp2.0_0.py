import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is a bit more involved than the others.  We need to test
# that the CFUNCTYPE instance is actually callable, and that the
# arguments to the callback are correct.  We also need to test that
# the prototype can be used to create a new CFUNCTYPE instance.
#
# The test is implemented by creating a CFUNCTYPE instance, and
# passing it as the callback to a function that calls the callback
# with a variety of arguments.  The callback function checks the
# arguments, and returns the result of the operation.
#
# The test function is implemented in C, and is called 'testfunc'.
# It is declared as follows:
#
#   int testfunc(int (*callback)(int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int,

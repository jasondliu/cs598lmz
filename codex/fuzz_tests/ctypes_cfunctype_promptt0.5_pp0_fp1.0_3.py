import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is a bit unusual in that it is not a standalone Python script.
# It is actually a part of a C program, and is invoked by main() in
# Modules/_ctypes/test/test_cfunctype.c.
#
# This test is useful because it exercises the argument processing logic
# in _ctypes.callproc, and the callback mechanism.
#
# The test works as follows:
#   - main() in the C program calls test_cfunctype() with a number of
#     arguments.
#   - test_cfunctype() creates a ctypes.CFUNCTYPE() instance, and
#     registers callback functions for each argument type.
#   - test_cfunctype() then iterates over the arguments, calling the
#     callback function for each argument.
#   - When the callback function is called, it checks that the data
#     passed from the C program is valid, and returns an integer
#     indicating success or failure.
#   - test_cfunctype() checks the return value from the callback,
#     and returns a failure

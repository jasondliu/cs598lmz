import ctypes
# Test ctypes.CFUNCTYPE
#
# This test case is based on the Python test case, test_cfuntype.py.
#
# This test case tests the following objects:
#
#   CFUNCTYPE
#
# It tests the following aspects of these objects:
#
#   - Creation of CFUNCTYPE objects with different signatures.
#   - Calling CFUNCTYPE objects with different signatures.
#   - Passing each of the supported parameter types.
#   - Passing pointers to each of the supported parameter types.
#   - Return each of the supported parameter types.
#   - Return a pointer to each of the supported parameter types.
#   - Verify that the Python types of the arguments are as expected.
#   - Passing a callable Python object as a callback.
#   - Passing invalid arguments to the callback.
#   - Passing a callable Python object as an argument to the callback.
#   - Passing a callable Python object as an argument to the callback,
#     and calling it in the callback.
#   - Calling the callback with invalid arguments.
#
# The following tests are not yet implemented:
#


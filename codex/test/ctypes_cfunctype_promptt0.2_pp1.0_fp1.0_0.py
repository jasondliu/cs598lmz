import ctypes
# Test ctypes.CFUNCTYPE()

# This is a test of ctypes.CFUNCTYPE()
#
# The test is to create a function pointer to a function that takes a
# double and returns a double.  The function pointer is then called
# with a double and the result is compared to the expected result.
#
# The test is run with the following types:
#
#    c_double, c_double
#    c_float, c_float
#    c_longdouble, c_longdouble
#    c_double, c_float
#    c_float, c_double
#    c_double, c_longdouble
#    c_longdouble, c_double
#    c_float, c_longdouble
#    c_longdouble, c_float
#
# The test is run with the following calling conventions:
#
#    cdecl
#    stdcall
#    fastcall
#
# The test is run with the following calling conventions:
#
#    cdecl
#    stdcall
#    fastcall
#
# The test is run with the following calling conventions:
#

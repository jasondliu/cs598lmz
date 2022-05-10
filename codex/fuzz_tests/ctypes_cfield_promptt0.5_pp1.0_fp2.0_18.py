import ctypes
# Test ctypes.CField.from_address()
#
# This test checks that the CField.from_address() method works correctly.
# The test passes if the output of the program is as listed below.
#
# The test consists of a C library, testlib.c, which contains a structure
# with a single integer field.  The test program, test_from_address.py,
# uses ctypes to load the library, and then calls the C function
# test_from_address(), which returns the address of the integer field in
# the structure.  The test program then calls CField.from_address() to
# create a ctypes instance from the address.  The address of the ctypes
# instance is checked against the address returned by the C function, and
# the value of the ctypes instance is checked against the expected value.
#
# The test passes if the addresses match and the value is as expected.
#
# The test is repeated twice.  The first time, the address is passed as
# an integer.  The second time, the address is passed as a ctypes object
# of type c_void_p.
#
# The

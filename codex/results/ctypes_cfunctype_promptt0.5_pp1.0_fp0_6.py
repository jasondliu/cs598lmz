import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is a little bit more complex than the other test, because we
# need to test the ctypes.CFUNCTYPE class.  This class is used to create
# callbacks functions.  These callbacks functions can be used as parameters
# to functions in shared libraries.
#
# We also need to test the ctypes.POINTER class.  This class is used to
# create pointers to other ctypes types.
#
# We also need to test the ctypes.c_void_p class.  This class is used to
# create void* pointers.
#
# We also need to test the ctypes.byref function.  This function is used
# to pass pointers to other ctypes types to functions in shared libraries.
#
# We also need to test the ctypes.cast function.  This function is used
# to cast pointers to other pointers.
#
# We also need to test the ctypes.memmove function.  This function is used
# to copy data from one location to another.
#
# We also need to test the ctypes.addressof function.  This function is

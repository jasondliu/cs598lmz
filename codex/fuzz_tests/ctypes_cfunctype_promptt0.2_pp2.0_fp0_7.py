import ctypes
# Test ctypes.CFUNCTYPE()

# This is a test of ctypes.CFUNCTYPE(), which is used to create C callback
# functions.  This test is based on the example in the Python ctypes
# documentation.

# http://docs.python.org/library/ctypes.html#ctypes.CFUNCTYPE

# The example in the documentation is for a callback function that takes
# two integers and returns an integer.  This test is for a callback function
# that takes two integers and returns a double.

# This test is for a callback function that takes two integers and returns
# a double.

import ctypes

# Define the callback function prototype.

# The callback function takes two integers and returns a double.

CALLBACK_FUNCTYPE = ctypes.CFUNCTYPE( ctypes.c_double, ctypes.c_int, ctypes.c_int )

# Define the callback function.

# The callback function takes two integers and returns a double.

def py_callback_func( x, y ):
    return float( x + y )

# Convert

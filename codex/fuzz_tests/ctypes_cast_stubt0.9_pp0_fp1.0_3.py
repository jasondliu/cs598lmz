import ctypes
ctypes.cast(0.0, ctypes.py_object)

# These are the standard definitions of the ctypes argument conversion
# functions.  They map Python types to C types, and they'll be used
# when passing arguments to the C function.  Extending the dictionary
# named 'argtypes' will allow us to convert other Python types to C
# types that our C functions understand.

from ctypes import c_int, c_long, c_float, c_double, c_char_p, py_object
from ctypes.util import find_library
from math import isnan

class method_type(object):
    pass

argtypes = {
    bool: c_int,
    int: c_int,
    long: c_long,
    float: c_double,
    method_type(isnan): c_int,
    }

class method_type(object):
    pass

def fast_try_str(s):
    try:
        return str(s)
    except:
        return s


class py_clang_type(object):
    def __

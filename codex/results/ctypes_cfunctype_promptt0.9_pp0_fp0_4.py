import ctypes
# Test ctypes.CFUNCTYPE
# The CFUNCTYPE factory requires a callable object that takes the proper number
# of positional arguments and returns a ctypes instance.
def int_to_type(i):
    """
    Return the ctypes type for the corresponding integral type.
    """
    if i == 1:
        return ctypes.c_byte
    elif i == 2:
        return ctypes.c_short
    elif i == 4:
        return ctypes.c_int
    elif i == 8:
        return ctypes.c_longlong
    else:
        raise ValueError('Not a valid integer typecode')

int_to_ptr = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)(
    lambda i: int_to_type(int(i)).in_dll(ctypes, '_ctypes_testfunc')
)

import numpy as np

np.ctypeslib.ctypes_function(int_to_ptr, np.ctypeslib.ndpointer(dtype=np.dtype(int)))



import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is a dummy function so that we can access the EFUNC
# global variable.
def _dummy_function():
    return EFUNC

# Set the location of the global variable in the _dummy_function.
EFUNC = ctypes.CFUNCTYPE(ctypes.c_int)
_dummy_function.__code__.co_consts = (_dummy_function.__code__.co_consts[0],
                                      EFUNC)

# Call the dummy function. This sets the EFUNC global variable.
_dummy_function()

# The following code is copied from ctypes/callbacks.py.
# This is the code that creates the C callback function.

from ctypes import _pointer_type_cache

def _check_flags(flags):
    from ctypes import CFUNCTYPE
    if not isinstance(flags, int):
        raise TypeError("flags must be integer")
    if (flags & CFUNCTYPE.FUNCFLAG_CDECL) and

import gc, weakref

from . import _cffi_backend


# ____________________________________________________________
#
# the following code is stolen from the pycparser project
# ____________________________________________________________

_C_TYPES = {
    'char' : 'c',
    'signed char' : 'b',
    'unsigned char' : 'B',
    'short' : 'h',
    'unsigned short' : 'H',
    'int' : 'i',
    'unsigned int' : 'I',
    'long' : 'l',
    'unsigned long' : 'L',
    'long long' : 'q',
    'unsigned long long' : 'Q',
    'float' : 'f',
    'double' : 'd',
    'long double' : 'g',
    '_Bool' : '?',
    }

def _get_ctype_from_dtype(dtype):
    """
    Returns the C type corresponding to the given numpy dtype.
    """
    if dtype.fields is not None:
        raise TypeError("un

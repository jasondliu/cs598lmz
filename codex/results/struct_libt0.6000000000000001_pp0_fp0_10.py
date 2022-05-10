import _struct

#-----------------------------------------------------------------------------
# Ctypes
#-----------------------------------------------------------------------------

# ctypes
try:
    import ctypes
except ImportError:
    ctypes = None

#-----------------------------------------------------------------------------
# Constants
#-----------------------------------------------------------------------------

# These are the types that we can handle
_typedict = {
    'char':              'c',
    'signed char':       'b',
    'unsigned char':     'B',
    'bytes':             's',
    'short':             'h',
    'unsigned short':    'H',
    'int':               'i',
    'unsigned int':      'I',
    'long':              'l',
    'unsigned long':     'L',
    'long long':         'q',
    'unsigned long long':'Q',
    'float':             'f',
    'double':            'd',
    'bool':              '?',
    'long double':       'g',
    'complex':           'F',
    'object':            'O',
    'string':            'S',
    'unicode':           '

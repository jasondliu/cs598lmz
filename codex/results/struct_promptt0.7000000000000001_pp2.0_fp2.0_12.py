import _struct
# Test _struct.Struct on struct module constants

# struct module constants
from test import struct_test

try:
    SIZE_OF_INT = _struct.calcsize('i')
except ImportError:
    SIZE_OF_INT = struct_test.SIZE_OF_INT

try:
    SIZE_OF_LONG = _struct.calcsize('l')
except AttributeError:
    SIZE_OF_LONG = struct_test.SIZE_OF_LONG

try:
    SIZE_OF_SHORT = _struct.calcsize('h')
except AttributeError:
    SIZE_OF_SHORT = struct_test.SIZE_OF_SHORT

try:
    SIZE_OF_FLOAT = _struct.calcsize('f')
except AttributeError:
    SIZE_OF_FLOAT = struct_test.SIZE_OF_FLOAT

try:
    SIZE_OF_DOUBLE = _struct.calcsize('d')
except AttributeError:
    SIZE_OF_DOUBLE = struct_test

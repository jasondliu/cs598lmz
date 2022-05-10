import _struct

import pytest


# constants for testing
_LITTLE_ENDIAN = '<'
_BIG_ENDIAN = '>'
_NATIVE_ENDIAN = '='
_PACK_INT = 'i'
_PACK_UNSIGNED_INT = 'I'
_PACK_SHORT = 'h'
_PACK_UNSIGNED_SHORT = 'H'
_PACK_CHAR = 'c'
_PACK_STRING = '5s'
_PACK_FLOAT = 'f'
_PACK_DOUBLE = 'd'
_PACK_LONG_LONG = 'q'
_PACK_UNSIGNED_LONG_LONG = 'Q'
_PACK_LONG = 'l'
_PACK_UNSIGNED_LONG = 'L'


# helpers
def get_test_cases():
    """Return a generator that produces a list of test cases.

    Each test case is a tuple that contains:
    - data to pack
    - struct format
    - struct format with native endian

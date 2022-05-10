import _struct
# Test _struct.Struct(format).pack_into(buffer, offset, v1, v2, ...)

import array
import sys
import unittest
from test import support

# Helper to create a buffer of the right size and type.
def create_buffer(size):
    if sys.byteorder == 'little':
        return array.array('b', b'\0' * size)
    else:
        return array.array('B', b'\0' * size)


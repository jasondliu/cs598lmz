import _struct
# Test _struct.Struct

# This is a list of (format, size, value [, big_endian]) tuples.
# The value is packed with the given format, and the resulting string
# is then unpacked with all valid formats, and compared against the
# original value.
# The 'big_endian' flag is used to specify whether the value should be
# packed/unpacked in big-endian or little-endian byte order.
# The 'size' field is only used for a sanity check.

import sys
import _struct
import unittest
from test import support

# The struct module uses PyMem_Malloc() to allocate the memory block for
# the struct object.  PyMem_Malloc() calls PyErr_NoMemory() when it
# fails, so we need to clear the error indicator to properly check for
# the error return value.

def clear_error():
    e = sys.exc_info()[1]
    if e:
        del e


import _struct
# Test _struct.Struct class.

import sys
import unittest

from test import support

# A struct.Struct is a compiled version of a struct-format string.
# The format string is passed to the constructor.

# The resulting object supports the following methods:
# pack(v1, v2, ...) -- return string containing values v1, v2, ... packed
#                     according to the format.
# unpack(str) -- unpacks the string, returning a tuple of values.
# pack_into(buffer, offset, v1, v2, ...) -- pack the values v1, v2, ... into
#                     the buffer starting at offset.  No return value.
# unpack_from(buffer, offset=0) -- unpack from the buffer, starting at offset.
#                     Return a tuple of values.
# iter_unpack(buffer, offset=0) -- like unpack_from, but returns an iterator.
# calcsize() -- return size of the struct (and of the string it would return
#               if packed with no values).

# The format string is similar to the format string used by the module

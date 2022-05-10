import _struct
# Test _struct.Struct.unpack_from() with format "s" and string longer than
# the size of the format.
#
# The bug is that the length of the string is checked against the size of
# the format, which is 1, instead of the length of the buffer.

import _struct

s = _struct.Struct("s")
b = b"abc"
# This should not raise an exception.
s.unpack_from(b, 0)
# This should raise an exception.
s.unpack_from(b, 1)

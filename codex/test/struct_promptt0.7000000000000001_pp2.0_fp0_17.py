import _struct
# Test _struct.Struct.pack_into() and pack_into_char_buffer().
import sys
import unittest
from test import support


def pack_into(st, fmt, buf, offset, *values):
    st.pack_into(buf, offset, *values)


class StructTest(unittest.TestCase):

    @support.impl_detail("test is specific to CPython")
    def test_pack_into_char_buffer(self):
        # Ensure that _struct.Struct.pack_into() accepts a writable buffer
        # as first argument.
        # _struct.Struct.pack_into(buffer, offset, v1, v2, ...)
        # _struct.Struct.pack_into_char_buffer(buffer, offset, v1, v2, ...)
        # are equivalent.
        args = (1, 2.0)
        st = _struct.Struct("i d")
        buf = bytearray(st.size)
        pack_into(st, "i d", buf, 0, *args)

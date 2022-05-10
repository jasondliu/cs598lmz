import _struct
# Test _struct.Struct.unpack_from using the new <Q and >Q format codes.
# These are in contrast to q and Q, which are reserved for Py_ssize_t.

import array
import _struct
import unittest
from test import support

@unittest.skipUnless(_struct.unpack_from, 'requires _struct.unpack_from')
class ByteOrderCheck:
    """Check byte order of < and > codes.  Run through a series of
    pack/unpack operations, checking whether the byte orders match.
    """

    def __init__(self, prefix, byteorder, big_endian_extensions):
        self.prefix = prefix
        self.byteorder = byteorder
        self.big_endian_extensions = big_endian_extensions

    def test(self, fmt, value):
        # Array to contain the value.
        a = array.array(self.prefix, [value])
        self.assertEqual(tuple(a), _struct.unpack(self.byteorder + fmt,
                                                  a.tostring()))
       

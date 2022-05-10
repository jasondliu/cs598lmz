import _struct
# Test _struct.Struct

import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct_unpack(self):
        # Test struct.unpack()
        self.assertEqual(_struct.unpack('i', b'abcd'), (1633837924,))
        self.assertEqual(_struct.unpack('i', b'efgh'), (1701074259,))
        self.assertEqual(_struct.unpack('i', b'ijkl'), (1768313494,))
        self.assertEqual(_struct.unpack('i', b'mnop'), (1835552729,))
        self.assertEqual(_struct.unpack('i', b'qrst'), (1902791964,))
        self.assertEqual(_struct.unpack('i', b'uvwx'), (1970031299,))
        self.assertEqual(_struct.unpack('i', b'yzab'), (2037270534,))
        self.assertEqual(_struct.unpack('i', b'c

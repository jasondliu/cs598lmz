import _struct
# Test _struct.Struct.
import unittest
from test import support

class StandardStructTestCase(unittest.TestCase):
    def test_standard_struct(self):
        # All standard formats should be available
        for t in [b'x', b'c', b'b', b'B', b'?', b'h', b'H', b'i', b'I', b'l',
                    b'L', b'q', b'Q', b'f', b'd', b's', b'p', b'P']:
            _struct.Struct(t)

    def test_standard_format(self):
        # Verify we can create standard format strings
        for t in [b'x', b'c', b'b', b'B', b'?', b'h', b'H', b'i', b'I', b'l',
                    b'L', b'q', b'Q', b'f', b'd', b's', b'p', b'P']:
            s = _struct.Struct(b'!' + t)
            self.assertEqual(s

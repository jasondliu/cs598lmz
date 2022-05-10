import _struct
# Test _struct.Struct.
import unittest
from test import support

def to_numbers(s):
    return _struct.unpack('%dh' % (len(s) // _struct.calcsize('h')), s)

class StructTest(unittest.TestCase):
    def test_new(self):
        s = _struct.Struct('i')
        self.assertEqual(s.format, 'i')
        self.assertEqual(s.size, _struct.calcsize('i'))
        self.assertRaises(TypeError, _struct.Struct)

    def test_get_newargs(self):
        s = _struct.Struct('i')
        self.assertEqual(s.__getnewargs__(), ('i',))
        self.assertEqual(_struct.Struct(*s.__getnewargs__()).format, 'i')

    def test_unpack(self):
        s = _struct.Struct('hhl')
        big_endian = (sys.byteorder == 'big')

        # Check byte order
        self.assert

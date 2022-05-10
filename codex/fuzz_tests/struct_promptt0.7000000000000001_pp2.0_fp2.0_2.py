import _struct
# Test _struct.Struct
import struct
import unittest

class StructTest(unittest.TestCase):
    def test_init(self):
        # _struct.Struct(fmt)
        Struct = _struct.Struct
        self.assertEqual(Struct("i").size, _struct.calcsize("i"))
        self.assertEqual(Struct("123456789012345678901234567890").size, 30)

        # _struct.Struct(fmt, /, *, <keyword arguments>)
        s = Struct("i", little_endian=True)
        self.assertEqual(s.size, _struct.calcsize("<i"))
        self.assertEqual(s.format, "<i")
        s = Struct("i", big_endian=True)
        self.assertEqual(s.size, _struct.calcsize(">i"))
        self.assertEqual(s.format, ">i")
        self.assertRaises(ValueError, Struct, "i", little_endian=True,
                          big_endian

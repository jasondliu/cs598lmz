import _struct
# Test _struct.Struct
import struct
import unittest

class StructTest(unittest.TestCase):
    def test_integers(self):
        # Test a range of integer formats
        for code in 'bBhHiIlLqQ':
            format = '=' + code
            s = _struct.Struct(format)
            self.assertEqual(s.size, struct.calcsize(format))
            for n in 0, 1, 2**8-1, 2**8, 2**15-1, 2**15, 2**16-1, 2**16, \
                2**31-1, 2**31, 2**32-1, 2**32, 2**63-1, 2**63, 2**64-1, 2**64:
                expected = struct.pack(format, n)
                self.assertEqual(s.pack(n), expected)
                self.assertEqual(s.pack_into(bytearray(s.size), 0, n), len(expected))
                self.assertEqual(s.unpack(expected), (n,))
               

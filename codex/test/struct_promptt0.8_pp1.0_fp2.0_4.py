import _struct
# Test _struct.Struct.pack() and .unpack()

import sys
import unittest

# Issue #23766
class MyStruct(tuple):
    def __new__(cls, *args):
        return tuple.__new__(cls, list(range(len(args))))

    def __repr__(self):
        return "MyStruct(*%r)" % tuple(self)


class PackTestCase(unittest.TestCase):
    fmt = 'hhl'
    s = _struct.Struct(fmt)
    size = s.size
    def test_unpack_from(self):
        data = b'abcdabcdabcdabcd'
        for i in range(len(data) - self.size + 1):
            x = self.s.unpack_from(data,i)
            self.assertEqual(x, (25185, 25699, 51348 + i))
            x = self.s.unpack(data[i:i+self.size])

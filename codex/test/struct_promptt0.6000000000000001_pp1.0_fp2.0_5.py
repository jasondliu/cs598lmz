import _struct
# Test _struct.Struct.iter_unpack, which was added in 3.7.

import _testcapi
import unittest

class StructIterUnpackTest(unittest.TestCase):

    def test_iter_unpack(self):
        with self.assertRaises(AttributeError):
            _struct.Struct('@I').iter_unpack
        with self.assertRaises(AttributeError):
            _struct.Struct('@I').iter_unpack(b'123')

        with self.assertRaises(ValueError):
            _struct.Struct('@I').iter_unpack(b'123', 0)
        with self.assertRaises(ValueError):
            _struct.Struct('@I').iter_unpack(b'123', 1)
        with self.assertRaises(ValueError):
            _struct.Struct('@I').iter_unpack(b'123', 2)
        with self.assertRaises(ValueError):
            _struct.Struct('@I').iter_unpack(b'123', 3)

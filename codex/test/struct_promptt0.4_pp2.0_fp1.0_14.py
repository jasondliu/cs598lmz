import _struct
# Test _struct.Struct class

# Test _struct.Struct class

import _struct
import unittest
from test import support

class StructTest(unittest.TestCase):

    def test_unpack_from(self):
        # Test unpacking from a buffer
        s = _struct.Struct('i')
        buf = bytes(range(4))
        self.assertEqual(s.unpack_from(buf, 0), (67305985,))
        self.assertEqual(s.unpack_from(buf, 0), (67305985,))
        self.assertEqual(s.unpack_from(buf, 0), (67305985,))
        self.assertEqual(s.unpack_from(memoryview(buf), 0), (67305985,))
        self.assertEqual(s.unpack_from(bytearray(buf), 0), (67305985,))
        self.assertEqual(s.unpack_from(buf, 0), (67305985,))

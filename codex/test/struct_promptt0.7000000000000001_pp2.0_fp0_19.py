import _struct
# Test _struct.Struct
from test import test_support
from test.test_support import verify

# Get the types supported in the struct module
import struct
if struct.calcsize("P") == 8:
    # 64-bit platform
    def add_types(L):
        L.append("q")
        L.append("Q")
else:
    # 32-bit platform
    def add_types(L):
        pass

types = []

add_types(types)

add_types(types)
add_types(types)
add_types(types)

class StructTest(unittest.TestCase):
    def test_ctor(self):
        s = _struct.Struct("i")
        self.assertEqual(s.size, 4)
        self.assertEqual(s.format, "i")

    def test_error_bad_type(self):
        self.assertRaises(TypeError, _struct.Struct, 42)

    def test_pack(self):
        s = _struct.Struct("i")

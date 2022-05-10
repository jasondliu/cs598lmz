import ctypes
# Test ctypes.CField
class CFieldTest(unittest.TestCase):
    def test_CField(self):
        # ctypes.CField.from_address
        cf = ctypes.CField.from_address(ctypes.addressof(ctypes.c_int(42)), ctypes.c_int)
        self.assertEqual(cf.value, 42)

    def test_CField_repr(self):
        cf = ctypes.CField.from_address(ctypes.addressof(ctypes.c_int(42)), ctypes.c_int)
        self.assertEqual(repr(cf), '<CField type=int, offset=0, size=4, ofsaddr=140733852392752, value=42>')

# Test ctypes.Array
class ArrayTest(unittest.TestCase):
    def test_array(self):
        # ctypes.Array
        class X(ctypes.Array):
            _length_ = 10
            _type_ = ctypes.c_int
        self.assertEqual(len

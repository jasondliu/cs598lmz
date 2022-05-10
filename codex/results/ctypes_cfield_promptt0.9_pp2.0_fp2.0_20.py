import ctypes
# Test ctypes.CField
class TestBuildValueErrorStructure(unittest.TestCase):
    def test_pack_two_char_in_int(self):
        class C(ctypes.Structure):
            _fields_ = [("name", ctypes.c_char * 2), ("value", ctypes.c_int)]
            _pack_ = 1

        v = C(b"a", 1)
        self.assertEqual(v.name, b"a\x00")
        self.assertEqual(v.value, 1)

        self.assertEqual(ctypes.sizeof(C), ctypes.sizeof(ctypes.c_int))

    def test_pack_two_char_in_int_with_offset(self):
        class C(ctypes.Structure):
            _fields_ = [("value", ctypes.c_int), ("name", ctypes.c_char * 2)]
            _pack_ = 1

        v = C(1, b"a")
        self.assertEqual(v.value, 1)
        self.assertEqual(

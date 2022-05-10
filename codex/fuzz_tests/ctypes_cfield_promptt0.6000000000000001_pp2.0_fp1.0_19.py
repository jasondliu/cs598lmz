import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield(self):
        class S(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int, 2),
                        ("c", ctypes.c_int, 0),
                        ("d", ctypes.c_int, 1)]
        self.assertEqual(ctypes.sizeof(S), ctypes.sizeof(ctypes.c_int))
        self.assertEqual(ctypes.alignment(S), ctypes.alignment(ctypes.c_int))
        self.assertEqual(S.a.offset, 0)
        self.assertEqual(S.b.offset, 0)
        self.assertEqual(S.c.offset, 0)
        self.assertEqual(S.d.offset, 0)
        self.assertEqual(S.a.bit_length, 32)
        self.assertEqual(S.b.bit_length, 2)
        self.assert

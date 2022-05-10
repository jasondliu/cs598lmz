import ctypes
# Test ctypes.CField
class CFieldTest(unittest.TestCase):
    def test_CField(self):
        class C(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(C.a.offset, 0)
        self.assertEqual(C.b.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(C.a.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(C.b.size, ctypes.sizeof(ctypes.c_int))

        self.assertEqual(C.a.index, 0)
        self.assertEqual(C.b.index, 1)

        self.assertEqual(C.a.name, "a")
        self.assertEqual(C.b.name, "b")

        self.assertEqual(C.a.ctype, ctypes.c_int)
        self.assertEqual(

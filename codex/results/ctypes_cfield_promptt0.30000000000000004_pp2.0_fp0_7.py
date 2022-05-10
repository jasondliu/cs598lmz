import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_simple(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]

        class RECT(ctypes.Structure):
            _fields_ = [("ul", POINT),
                        ("lr", POINT)]

        class CFIELD(ctypes.Structure):
            _fields_ = [("rect", RECT),
                        ("name", ctypes.c_char * 32)]

        cfield = CFIELD()
        self.assertEqual(cfield.name, b"\0" * 32)
        self.assertEqual(cfield.rect.ul.x, 0)
        self.assertEqual(cfield.rect.ul.y, 0)
        self.assertEqual(cfield.rect.lr.x, 0)
        self.assertEqual(cfield.rect.lr.y, 0)

        cfield.rect.ul.x = 10
        cfield

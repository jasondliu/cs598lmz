import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield(self):
        # Test ctypes.CField
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
            def __init__(self):
                self.a = 1
                self.b = 2

        x = X()
        self.assertEqual(x.a, 1)
        self.assertEqual(x.b, 2)
        self.assertEqual(ctypes.sizeof(x), ctypes.sizeof(ctypes.c_int) * 2)

        # Test ctypes.CField.offset
        self.assertEqual(ctypes.c_int.offset, 0)
        self.assertEqual(ctypes.c_int.in_dll(x, "a").offset, 0)
        self.assertEqual(ctypes.c_int.in_dll(x, "b").offset, ctypes.sizeof(ctypes.c_

import ctypes
# Test ctypes.CField

class TestCField(unittest.TestCase):
    def test_basic(self):
        import _ctypes_test
        class X(ctypes.Structure):
            _fields_ = [('a', ctypes.c_int),
                        ('b', ctypes.c_char),
                        ('c', ctypes.c_int)]
        X._pack_ = 1
        self.assertEqual(ctypes.sizeof(X), 7)
        self.assertEqual(ctypes.alignment(X), 1)

        x = X()
        self.assertEqual(x.a, 0)
        self.assertEqual(x.b, b'\x00')
        self.assertEqual(x.c, 0)

        x.a = 1
        x.b = b'\x02'
        x.c = 3
        self.assertEqual(x.a, 1)
        self.assertEqual(x.b, b'\x02')
        self.assertEqual(x.c, 3)

    def test_

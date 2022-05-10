import ctypes
# Test ctypes.CField

class TestCField(unittest.TestCase):

    def test_int(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int),
                        ("c", ctypes.c_int),
                        ("d", ctypes.c_int),
                        ("e", ctypes.c_int)]

            def __init__(self):
                self.a = 1
                self.b = 2
                self.c = 3
                self.d = 4
                self.e = 5

        self.assertEqual(ctypes.sizeof(X), 20)
        x = X()
        self.assertEqual(x.a, 1)
        self.assertEqual(x.b, 2)
        self.assertEqual(x.c, 3)
        self.assertEqual(x.d, 4)
        self.assertEqual(x.e, 5)

        x.a = 100
        x.b = 200
        x.c

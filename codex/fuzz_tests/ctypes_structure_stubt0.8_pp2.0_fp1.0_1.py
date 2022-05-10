import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long()
    y = ctypes.c_long()

    def __str__(self):
        return "S(%r, %r)" % (self.x, self.y)

    def __repr__(self):
        return str(self)

class TestType(unittest.TestCase):
    def test_int(self):
        self.assertEqual(ctypes.sizeof(ctypes.c_int), 4)
        # the offset of x will be 4, not 3, on a 64-bit platform.  sizeof
        # will be 8.
        class S(ctypes.Structure):
            _fields_ = [("x", ctypes.c_byte),
                        ("y", ctypes.c_int)]

        self.assertEqual(ctypes.sizeof(S), 4)
        self.assertEqual(S().y, 0)
        self.assertEqual(S(42).y, 42)
        self.assertRaises(TypeError, S, "hello")
        self.assertRaises(TypeError

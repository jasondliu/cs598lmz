import ctypes
# Test ctypes.CField

class CTest(ctypes.Structure):
    _fields_ = [("a", ctypes.CField),
                ("b", ctypes.CField),
                ("c", ctypes.CField),
                ("d", ctypes.CField)]

class Test(unittest.TestCase):
    def test_sizeof(self):
        self.assertEqual(ctypes.sizeof(CTest), 4)

    def test_getattr(self):
        t = CTest()
        self.assertEqual(t.a, 0)
        self.assertEqual(t.b, 0)
        self.assertEqual(t.c, 0)
        self.assertEqual(t.d, 0)

    def test_setattr(self):
        t = CTest()
        t.a = 1
        t.b = 2
        t.c = 3
        t.d = 4
        self.assertEqual(t.a, 1)
        self.assertEqual(t.b, 2)
        self.assertEqual(

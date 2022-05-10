import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    class CFieldTest(ctypes.Structure):
        _fields_ = [
            ("a", ctypes.CField, 1),
            ("b", ctypes.CField, 1),
            ("c", ctypes.CField, 1),
            ("d", ctypes.CField, 5),
            ("e", ctypes.CField, 1),
            ("f", ctypes.CField, 1),
        ]

    def test_cfield(self):
        t = self.CFieldTest()
        t.a = 2
        t.b = 3
        t.c = 4
        t.d = 5
        t.e = 6
        t.f = 7

        self.assertEqual(t.a, 2)
        self.assertEqual(t.b, 3)
        self.assertEqual(t.c, 4)
        self.assertEqual(t.d, 5)
        self.assertEqual(t.e, 6)
        self.assertEqual(t.

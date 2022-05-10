import ctypes
# Test ctypes.CField
class TestCFied(unittest.TestCase):

    def test_simple(self):
        class C(ctypes.Structure):
            _fields_ = [
                ("a", ctypes.c_int),
                ("b", ctypes.c_int)]
        x = C()
        x.a = 1
        x.b = 2

        n = ctypes.sizeof(C)
        self.assertEqual(8, n)

    def test_bitfields(self):
        class BitField(ctypes.Structure):
            _fields_ = [
                ("a", ctypes.c_int, 8),
                ("b", ctypes.c_int, 8),
                ("c", ctypes.c_int, 8),
                ("d", ctypes.c_int, 8)]
        x = BitField()
        x.a = 1
        self.assertEqual(1, x.a)
        self.assertEqual(0, x.b)
        self.assertEqual(0, x.c)
        self.assertEqual

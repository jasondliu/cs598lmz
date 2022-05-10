import ctypes
# Test ctypes.CField
import ctypes._testcapi as _testcapi

class TestField(unittest.TestCase):
    def test_S(self):
        class U(ctypes.Union):
            _fields_ = [
                ('a', ctypes.c_int),
                ('b', ctypes.c_short),
                ('c', ctypes.c_char)
            ]

        self.assertEqual(ctypes.sizeof(U), ctypes.c_int.size)
        x = U()
        self.assertEqual(ctypes.addressof(x), ctypes.addressof(x.a))

    def test_S2(self):
        class U(ctypes.Union):
            _fields_ = [
                ('a', ctypes.c_int),
                ('b', ctypes.c_short),
                ('c', ctypes.c_char * 2)
            ]

        self.assertEqual(ctypes.sizeof(U), ctypes.c_int.size)
        x = U()
        self.assertEqual

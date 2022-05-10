import ctypes
# Test ctypes.CField
# See http://docs.python.org/3.3/library/ctypes.html#ctypes.CField

class TestCF(unittest.TestCase):
    def test_c_field(self):
        # See http://docs.python.org/3.3/library/ctypes.html#ctypes._CFuncPtr.errcheck
        class B(ctypes.LittleEndianStructure):
            _fields_ = [
                ('d', ctypes.c_char),
                ('c', ctypes.c_short),
                ('b', ctypes.c_int),
                ('a', ctypes.c_longlong),
            ]
        self.assertEqual(B.a.offset, ctypes.sizeof(ctypes.c_longlong))
        self.assertEqual(B.b.offset, ctypes.sizeof(ctypes.c_longlong) + ctypes.sizeof(ctypes.c_int))
        self.assertEqual(B.c.offset, ctypes.sizeof(ctypes.c_longlong) + c

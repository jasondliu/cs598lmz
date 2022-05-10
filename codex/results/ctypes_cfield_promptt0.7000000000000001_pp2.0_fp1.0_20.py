import ctypes
# Test ctypes.CField

class TestCField(unittest.TestCase):
    def test_simple(self):
        class S(ctypes.Structure):
            _fields_ = [('a', ctypes.c_int)]

        class X(ctypes.Union):
            _fields_ = [('b', ctypes.c_float),
                        (ctypes.c_int, ctypes.c_int)]

        class C(ctypes.Structure):
            _fields_ = [('s', S),
                        ('x', X)]

        self.assertEqual(C._fields_, [('s', S), ('x', X)])

        # self.assertEqual(C.s.offset, 0)
        self.assertEqual(C.x.offset, ctypes.sizeof(S))
        self.assertEqual(C.x.size, ctypes.sizeof(ctypes.c_float))

    def test_name_index(self):
        class S(ctypes.Structure):
            _fields_ = [('a', ctypes.c_int)]



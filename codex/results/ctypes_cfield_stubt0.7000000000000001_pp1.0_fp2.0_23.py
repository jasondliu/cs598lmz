import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', ctypes.c_int),
                ('d', ctypes.c_int)]

class Test(unittest.TestCase):

    def test_offsetof(self):
        offset = ctypes.offsetof(S, 'x')
        self.assertEqual(ctypes.sizeof(S), ctypes.sizeof(ctypes.c_int))
        self.assertEqual(offset, 0)

    def test_c_uint(self):
        from ctypes import c_uint
        self.assertEqual(c_uint(0x80000000).value, 0x80000000)
        self.assertEqual(c_uint(0xFFFFFFFF).value, 0xFFFFFFFF)
        self.assertEqual(c_uint(1 << 32).value, 1)
        self.assertEqual(c_uint(1 << 64).value, 1)

    def test_

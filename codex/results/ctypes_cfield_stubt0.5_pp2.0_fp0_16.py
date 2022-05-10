import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFoo:
    pass

ctypes.CFuncPtr = type(CFoo.__call__)

class Test(unittest.TestCase):
    def test_c_int(self):
        self.assertEqual(ctypes.c_int.__module__, 'ctypes')

    def test_c_void_p(self):
        self.assertEqual(ctypes.c_void_p.__module__, 'ctypes')

    def test_c_char_p(self):
        self.assertEqual(ctypes.c_char_p.__module__, 'ctypes')

    def test_c_wchar_p(self):
        self.assertEqual(ctypes.c_wchar_p.__module__, 'ctypes')

    def test_c_byte(self):
        self.assertEqual(ctypes.c_byte.__module__, 'ctypes')

    def test_c_ubyte(self):
        self.assertEqual(ctypes.c_ubyte.__module

import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class MyType(object):
    def from_param(self, param):
        return param

ctypes.CFuncPtr = type(ctypes.cast)

MyTypePtr = ctypes.POINTER(MyType)

ctypes.CArray = type(S * 3)

class TestCase(unittest.TestCase):

################################################################
# Test Ctypes Types

# The type of 'ctypes.c_void_p' is 'class 'ctypes.LP_c_void'
    def test_type_of_c_void_p(self):
        self.assertEqual(ctypes.c_void_p, ctypes.LP_c_void)

# The type of 'ctypes.c_char_p' is 'class 'ctypes.LP_c_char'
    def test_type_of_c_char_p(self):
        self.assertEqual(ctypes.c_char_p, ctypes.LP_c_char)

# The type of 'ctypes.c_wchar_p' is 'class

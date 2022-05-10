import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def make_c_type_test(typ):
    def test(self):
        assert isinstance(typ, ctypes.c_type)
        assert issubclass(typ, ctypes.CField)
    return test

class test_c_type(TestCase):

    test_ctypes = make_c_type_test(ctypes.ctypes)

    test_c_bool = make_c_type_test(ctypes.c_bool)
    test_c_byte = make_c_type_test(ctypes.c_byte)
    test_c_char = make_c_type_test(ctypes.c_char)
    test_c_char_p = make_c_type_test(ctypes.c_char_p)
    test_c_double = make_c_type_test(ctypes.c_double)
    test_c_float = make_c_type_test(ctypes.c_float)
    test_c_int = make_c_type_test(ctypes.c_int)
    test

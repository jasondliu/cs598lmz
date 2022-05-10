import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):

    def test_overflow(self):
        for type_ in [ctypes.c_byte, ctypes.c_ubyte,
                      ctypes.c_short, ctypes.c_ushort,
                      ctypes.c_int, ctypes.c_uint,
                      ctypes.c_long, ctypes.c_ulong,
                      ctypes.c_longlong, ctypes.c_ulonglong]:
            integer = _ctypes_test.make_int_instance(type_)
            type_info = ctypes.get_type_info(type_)
            self.assertRaises(ValueError, type_info.set_value, integer,
                              2*sys.maxint+1)
            self.assertRaises(ValueError, type_info.set_value, integer,
                              -2*sys.maxint-1)
        type_ = ctypes.c_int
        integer = _ctypes_test.make_int_instance(type_)
        type_info = c

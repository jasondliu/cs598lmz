import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S2(ctypes.Structure):
    pass

class S3(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int), ('z', ctypes.c_int)]

class Test_update_fields(BaseTestCase):
    def test_empty(self):
        s = S2()
        self.assertEqual(s._fields_, [])
        s._fields_ = [('foo', ctypes.c_int), ('bar', ctypes.c_int)]
        self.assertEqual(s._fields_, [('foo', ctypes.c_int), ('bar', ctypes.c_int)])

    def test_identity(self):
        s = S3()
        self.assertEqual(s._fields_, [('x', ctypes.c_int), ('y', ctypes.c_int),
                                      ('z', ctypes.c_int)])
        s._fields_ = s._fields_[:]
        self.assertE

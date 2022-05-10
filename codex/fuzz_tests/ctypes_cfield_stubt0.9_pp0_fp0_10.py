import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFieldTestCase(unittest.TestCase):
    def test_type(self):

        class X(ctypes.Structure):
            _fields_ = [('f', ctypes.c_int)]

        self.assertEquals(X.f.__class__, ctypes.CField)

    def test_convert(self):
        self.assertEquals(S.x._ctype_, ctypes.c_int)
        self.assertEquals(S.x.from_param, ctypes.c_int.from_param)
        self.assertEquals(S.x.from_address, ctypes.c_int.from_address)
        self.assertEquals(S.x.size, ctypes.c_int.size)

    def test_restype(self):
        def f(x):
            return x
        ctypes.pythonapi.PyObject_GetAttrString.restype = S.x
        self.assertEquals(type(ctypes.pythonapi.PyObject_GetAttrString(1)),
                

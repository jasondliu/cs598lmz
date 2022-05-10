import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

ctypes.pythonapi.PyType_IsSubtype.restype = ctypes.c_int
ctypes.pythonapi.PyType_IsSubtype.argtypes = [ctypes.py_object, ctypes.py_object]

def issubclass(cls1, cls2):
    if type(cls1) == ctypes.CField and type(cls2) == ctypes.CField:
        return cls2.__dict__.get('_type_', cls1._type_) is cls1._type_
    return ctypes.pythonapi.PyType_IsSubtype(cls1, cls2)

class TestCtypes(unittest.TestCase):
    def test_issubclass(self):
        self.assertTrue(issubclass(ctypes.c_int, ctypes.c_int))
        self.assertTrue(issubclass(ctypes.c_int, ctypes.c_long))
        self.assertFalse(issubclass(ctypes.c_long, ctypes.c_int))

import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class MyField(ctypes.CField):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.offset = None

class MyStructure(ctypes.Structure):
    _fields_ = [('x', MyField(ctypes.c_int))]

class MyUnion(ctypes.Union):
    _fields_ = [('x', MyField(ctypes.c_int))]

class MyArray(ctypes.Array):
    _type_ = MyField(ctypes.c_int)

class MyPointer(ctypes.POINTER(ctypes.c_int)):
    _type_ = MyField(ctypes.c_int)


class Test(unittest.TestCase):

    def test_structure(self):
        s = MyStructure()
        self.assertEqual(s.x.offset, 0)
        self.assertEqual(s.x.offset, 0)

    def test_union(self):
        s = MyUnion()

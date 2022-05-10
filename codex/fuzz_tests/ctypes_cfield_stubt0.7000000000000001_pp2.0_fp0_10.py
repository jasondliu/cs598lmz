import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def _c_field_is(self, f):
    return f is self

ctypes.CField.__eq__ = _c_field_is
ctypes.CField.__ne__ = lambda self, f: not self == f

def _c_field_hash(self):
    return hash(self.name)

ctypes.CField.__hash__ = _c_field_hash


class CFieldTest(unittest.TestCase):
    def test(self):
        f = ctypes.CField("x", ctypes.c_int, 0)
        g = ctypes.CField("x", ctypes.c_int, 0)
        self.assertEqual(f, f)
        self.assertEqual(f, g)
        self.assertNotEqual(f, None)
        self.assertNotEqual(f, "")
        self.assertEqual(hash(f), hash(g))
        self.assertEqual(hash(f), hash(g))

        # hash(f) is not -1, so

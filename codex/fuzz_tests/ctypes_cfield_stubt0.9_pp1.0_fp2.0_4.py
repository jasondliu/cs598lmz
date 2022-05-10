import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def f(apply, kw):
    for op, cls in [('__mul__', ctypes.CField),
                    ('__rmul__', ctypes.c_int),
                    ('__rmul__', ctypes.CField),
                    ('__imul__', S)]:
        apply(op, ({'cls': cls},), kw)

class TestCField(unittest.TestCase):
    @support.cpython_only
    def test_type(self):
        with self.assertRaises(TypeError):
            type(S).x / 1
        with self.assertRaises(TypeError):
            type(S).x / type(S).x
        with self.assertRaises(TypeError):
            type(S).x // 1
        with self.assertRaises(TypeError):
            type(S).x // type(S).x
        with self.assertRaises(TypeError):
            type(S).x % 1
        with self.assertRaises(TypeError):
            type(S).x % type

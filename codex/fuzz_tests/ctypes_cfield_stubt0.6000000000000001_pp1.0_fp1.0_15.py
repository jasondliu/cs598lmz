import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_getattr(self):
    class C(ctypes.Structure):
        _fields_ = [("foo", ctypes.c_int)]
    c = C()
    self.assertEqual(c.foo, 0)
    c.foo = 42
    self.assertEqual(c.foo, 42)

def test_setattr(self):
    class C(ctypes.Structure):
        _fields_ = [("foo", ctypes.c_int)]
    c = C()
    c.foo = "hello"
    self.assertEqual(c.foo, ord("h"))

def test_setattr_fail(self):
    class C(ctypes.Structure):
        _fields_ = [("foo", ctypes.c_int)]
    c = C()
    self.assertRaises(TypeError, setattr, c, "foo", "hello")

def test_c_char_p(self):
    class C(ctypes.Structure):
        _fields_ = [("foo", ctypes.c_

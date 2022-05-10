import ctypes
# Test ctypes.CField class


class X(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]


class Y(X):
    _fields_ = [('y', ctypes.c_int)]


class Foo(ctypes.c_int):
    _fields_ = [('bar', ctypes.c_int)]


x = X()
y = Y()
foo = Foo(0)


class TestField(unittest.TestCase):

    def test_basics(self):
        self.assertEqual(X.x.offset, 0)
        self.assertEqual(X.x._name, 'x')
        self.assertEqual(X.x._type_, ctypes.c_int)
        self.assertEqual(y.y.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(y.y._name, 'y')
        self.assertEqual(y.y._type_, ctypes.c_int)
        self.assertEqual(y.x._

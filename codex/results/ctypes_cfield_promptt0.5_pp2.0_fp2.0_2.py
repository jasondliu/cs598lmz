import ctypes
# Test ctypes.CField

import ctypes.test.test_cf

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y),
                ("z", ctypes.c_int)]

class Test(ctypes.test.test_cf.StructureTestCase):
    def test_cfield(self):
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(Y.x.offset, 0)
        self.assertEqual(Y.y.offset, ctypes.sizeof(X))
        self.assertEqual(Z.y.offset, 0)
        self.assertEqual(Z

import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, x):
        self.x = x

CField = type(C.x)

def test_fields(self):
    class X(ctypes.Structure):
        _fields_ = [("a", ctypes.c_int)]
    self.assertEqual(X._fields_, [("a", ctypes.c_int)])
    self.assertEqual(X._fields_[0][0], "a")
    self.assertEqual(X._fields_[0][1], ctypes.c_int)

    class Y(ctypes.Structure):
        _fields_ = [("a", ctypes.c_int),
                    ("b", ctypes.c_double)]
    self.assertEqual(Y._fields_, [("a", ctypes.c_int),
                                  ("b", ctypes.c_double)])
    self.assertEqual(Y._fields_[0][0], "a")
    self.assertEqual(Y._fields_[0][

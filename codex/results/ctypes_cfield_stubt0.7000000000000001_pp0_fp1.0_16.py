import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CFieldType = type(S._fields_[0])

class Test(unittest.TestCase):

    def test_subclass(self):
        class A(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int)]
        class B(A):
            _fields_ = [("y", ctypes.c_int)]
        self.assertEqual(len(B._fields_), 2)
        self.assertEqual([f[0] for f in B._fields_], ["x", "y"])

    def test_substruct(self):
        class A(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int)]
        class B(ctypes.Structure):
            _fields_ = [("a", A), ("y", ctypes.c_int)]
        self.assertEqual(len(B._fields_), 2)
        self.assertEqual([f[0] for f in B._fields_], ["a", "y"])

    def test_

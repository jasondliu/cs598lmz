import ctypes
# Test ctypes.CFUNCTYPE:
c_int_p = ctypes.POINTER(ctypes.c_int)
def testCFUNCTYPE(self):
    c_testfunc = ctypes.CFUNCTYPE(ctypes.c_int, c_int_p)
    class X(ctypes.Structure):
        _fields_ = [("func", c_testfunc)]
    self.assertEqual(X.func.restype, ctypes.c_int)
    self.assertEqual(X.func.argtypes, (c_int_p,))
    #
    class Y(ctypes.Structure):
        _fields_ = [("value", ctypes.c_int),
                    ("func", c_testfunc)]
    self.assertEqual(Y.func.restype, ctypes.c_int)
    self.assertEqual(Y.func.argtypes, (c_int_p,))
    #
    class Z(ctypes.Structure):
        _fields_ = [("values", c_int_p),
                    ("func", c_

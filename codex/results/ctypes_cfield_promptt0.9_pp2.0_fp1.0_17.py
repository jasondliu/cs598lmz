import ctypes
# Test ctypes.CField implementation.

class TestCFuncPtr(unittest.TestCase):
    def test_ptr(self):
        # first test
        class X(ctypes.Structure):
            pass
        X._fields_ = [("f", ctypes.CField(X))]
        f = ctypes.c_void_p.in_dll(ctypes, "f")

        x = X()
        x.f = x
        self.assertEqual(x.f, x)

        # no more recursive definitions
        class Y(ctypes.Structure):
            _fields_ = [("f", ctypes.c_void_p)]

        self.assertRaises((TypeError, AttributeError), setattr, Y, "_fields_",
                          [("f", ctypes.CField(X))]
                          )
        class Y(ctypes.Structure):
            _fields_ = [("f", ctypes.c_void_p)]
            def setfield(self, f):
                self.f = f

        try:
            Y().setfield(f)

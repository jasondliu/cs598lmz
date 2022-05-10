import ctypes
# Test ctypes.CField()
import ctypes.test.test_cfield


class CFunctionTest(unittest.TestCase):
    def test_argtypes(self):
        self.assertRaises(TypeError, ctypes.CFUNCTYPE, None, ctypes.c_int)
        self.assertRaises(TypeError, ctypes.CFUNCTYPE, None)

    def test_restype(self):
        ctypes.CFUNCTYPE(None, ctypes.c_int)
        ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
        self.assertRaises(TypeError, ctypes.CFUNCTYPE, ctypes.c_int)

    def test_call_wrong_argtypes(self):
        def wrongargs(x):
            pass
        prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.assertRaises(TypeError, prototype, wrongargs)

    def test_call_missing_argtypes(

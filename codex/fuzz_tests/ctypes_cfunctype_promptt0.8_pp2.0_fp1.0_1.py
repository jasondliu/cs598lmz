import ctypes
# Test ctypes.CFUNCTYPE
class TestCFUNCTYP(unittest.TestCase):
    def test_basic(self):
        from _ctypes import PyObj_FromPtr
        NULL = ctypes.c_void_p()
        pyfunc = PyObj_FromPtr(NULL)
        f = ctypes.CFUNCTYPE(None, ctypes.c_int)()
        self.assertRaises(TypeError, f)
        self.assertRaises(TypeError, f, None)
        f.restype = ctypes.c_int
        f.argtypes = [ctypes.c_int]
        self.assertEqual(f(42), 0)

def func(i):
    return i + 1

class Test_CFUNCTYPE(unittest.TestCase):
    def test_call(self):
        f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)
        self.assertEqual(f(41), 42)

    def test_cache(self):
        from _ctypes import CF

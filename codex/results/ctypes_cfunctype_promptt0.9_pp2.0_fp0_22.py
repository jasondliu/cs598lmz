import ctypes
# Test ctypes.CFUNCTYPE(ctypes.POINTER(None))(None)
# Test ctypes.CFUNCTYPE(ctypes.POINTER(None))(("a", None))
# Test ctypes.CFUNCTYPE(ctypes.POINTER(None))((("a", None), None))
# Test ctypes.CFUNCTYPE(ctypes.POINTER(None))((("a", None), ("b", None)))
# Test ctypes.CFUNCTYPE(ctypes.POINTER(None))((("a", None), ("b", None), None))

@skip("manual, #274")
class TestCFunctionType(unittest.TestCase):
    def test_argtypes(self):
        prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

        def func(*args, **kwds):
            return 42

        self.assertRaises(TypeError, prototype, func)
        func.__annotations__ = {'argtypes': (ctypes.c_int, ctypes.c

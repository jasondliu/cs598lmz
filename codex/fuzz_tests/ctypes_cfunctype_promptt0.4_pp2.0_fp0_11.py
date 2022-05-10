import ctypes
# Test ctypes.CFUNCTYPE(None)(lambda: None)

class TestCFUNCTYPE(unittest.TestCase):

    def test_callable(self):
        def f():
            pass
        self.assertTrue(callable(ctypes.CFUNCTYPE(None)(f)))

    def test_call(self):
        def f():
            pass
        self.assertIsNone(ctypes.CFUNCTYPE(None)(f)())

    def test_args(self):
        def f(x):
            return x
        self.assertEqual(ctypes.CFUNCTYPE(None, ctypes.c_int)(f)(42), 42)
        self.assertEqual(ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)(f)(42, 43), 42)

    def test_restype(self):
        def f():
            return 42
        self.assertEqual(ctypes.CFUNCTYPE(ctypes.c_int)(f)(), 42)

    def test_argtypes(self):

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class Test(unittest.TestCase):
    def test_basic(self):
        def f():
            pass
        self.assertEqual(type(f), types.FunctionType)
        self.assertEqual(type(f), FUNTYPE)
        self.assertEqual(type(f), FUNTYPE(f))

    def test_simple(self):
        self.assertEqual(repr(FUNTYPE), "<class 'ctypes.CFUNCTYPE'>")
        self.assertEqual(FUNTYPE(lambda: None), FUNTYPE)

    def test_callable(self):
        self.assertTrue(callable(FUNTYPE))

    def test_subclass(self):
        class Sub(FUNTYPE):
            pass
        self.assertEqual(Sub(lambda: None), FUNTYPE)
        self.assertEqual(Sub(lambda: None), FUNTYPE(lambda: None))

    def test_subclass_with_kwargs(self):
        class Sub(FUNTYPE):
            def __new__(cls, *args, **kwargs

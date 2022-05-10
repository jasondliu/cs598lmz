import types
# Test types.FunctionType

class TestFunctionType(unittest.TestCase):
    def test_function_type(self):
        def f(): pass
        self.assertTrue(type(f) is types.FunctionType)
        self.assertTrue(type(f) is types.BuiltinFunctionType)
        self.assertTrue(type(type) is types.BuiltinFunctionType)
        self.assertTrue(type(type) is types.TypeType)
        self.assertTrue(type(type(type)) is types.TypeType)

    def test_function_attrs(self):
        def f(): pass
        self.assertTrue(hasattr(f, '__code__'))
        self.assertTrue(hasattr(f, '__doc__'))
        self.assertTrue(hasattr(f, '__name__'))
        self.assertTrue(hasattr(f, '__defaults__'))
        self.assertTrue(hasattr(f, '__module__'))
        self.assertTrue(hasattr(f, '__dict__'))
        self.assertTrue

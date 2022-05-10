import types
# Test types.FunctionType
class Test_FunctionType(unittest.TestCase):
    def test_FunctionType(self):
        def foo():
            pass

        self.assertEqual(type(foo), types.FunctionType)

# Test types.BuiltinFunctionType
class Test_BuiltinFunctionType(unittest.TestCase):
    def test_BuiltinFunctionType(self):
        self.assertEqual(type(len), types.BuiltinFunctionType)

# Test types.MethodType
class Test_MethodType(unittest.TestCase):
    def test_MethodType(self):
        def foo():
            pass

        class A:
            def __init__(self):
                self.foo = foo
                self.bar = types.MethodType(foo, self)

        a = A()
        self.assertEqual(type(a.foo), types.MethodType)
        self.assertEqual(type(a.bar), types.MethodType)

# Test types.BuiltinMethodType
class Test_BuiltinMethodType(unittest.TestCase):
    def

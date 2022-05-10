import types
# Test types.FunctionType
class function_type_test(unittest.TestCase):
    def test_function_type(self):
        def f(): pass
        self.assertEqual(type(f), types.FunctionType)


# Test types.BuiltinFunctionType
class builtin_function_type_test(unittest.TestCase):
    def test_builtin_function_type(self):
        self.assertEqual(type(abs), types.BuiltinFunctionType)

    def test_builtin_function_type_abs(self):
        self.assertEqual(type(abs), types.BuiltinFunctionType)

    def test_builtin_function_type_all(self):
        self.assertEqual(type(all), types.BuiltinFunctionType)

    def test_builtin_function_type_any(self):
        self.assertEqual(type(any), types.BuiltinFunctionType)

    def test_builtin_function_type_ascii(self):
        self.assertEqual(type(ascii), types.BuiltinFunctionType)



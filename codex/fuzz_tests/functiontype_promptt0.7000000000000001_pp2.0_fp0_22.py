import types
# Test types.FunctionType and types.LambdaType
class TestFunctionAndLambda(unittest.TestCase):
    def test_function_creation(self):
        def f(): pass
        self.assertIs(type(f), types.FunctionType)

    def test_lambda_creation(self):
        f = lambda : None
        self.assertIs(type(f), types.LambdaType)

    def test_function_attributes(self):
        def f(): pass

        self.assertIs(f.__class__, types.FunctionType)
        self.assertEqual(f.__name__, 'f')
        self.assertEqual(f.__code__.co_name, 'f')
        self.assertEqual(f.__code__.co_argcount, 0)
        self.assertIs(type(f.__globals__), dict)
        self.assertIs(type(f.__defaults__), tuple)
        #self.assertIs(type(f.__closure__), types.CellType) # CPython only
        self.assertE

import types
# Test types.FunctionType() and types.LambdaType()
#
# Note: types.LambdaType() is no longer available in Python 3.0,
# instead the function type lambda expression is used.

def is_lambda_type(obj):
    return isinstance(obj, types.LambdaType)

class TestTypes(TestCase):

    def test_functiontype(self):
        self.assertEqual(types.FunctionType, type(lambda x: x))
        self.assertEqual(types.FunctionType, type(lambda x: x).__class__)

    def test_lambdatype(self):
        if sys.version_info[0] >= 3:
            self.assertRaises(AttributeError, lambda: types.LambdaType)
        else:
            self.assertEqual(types.LambdaType, type(lambda x: x))
            self.assertEqual(types.LambdaType, type(lambda x: x).__class__)

    def test_is_lambda_type(self):
        self.assertTrue(is_lambda_type

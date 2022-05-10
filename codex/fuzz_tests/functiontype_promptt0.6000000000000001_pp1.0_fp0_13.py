import types
# Test types.FunctionType and types.LambdaType for Python 2 and Python 3 compatibility.
if sys.version_info < (3, 0):
    FunctionType = types.FunctionType
    LambdaType = types.LambdaType
else:
    FunctionType = types.FunctionType
    LambdaType = types.LambdaType


class Test_decorator(unittest.TestCase):

    def test_default_decorator(self):
        """Test that the default decorator works as expected."""
        @default
        def func1(a, b, c=3):
            return a, b, c

        self.assertEqual(func1(1, 2), (1, 2, 3))

        @default
        def func2(a, b, c=3, d=4):
            return a, b, c, d

        self.assertEqual(func2(1, 2), (1, 2, 3, 4))
        self.assertEqual(func2(1, 2, d=7), (1, 2, 3, 7))
        self.assertEqual

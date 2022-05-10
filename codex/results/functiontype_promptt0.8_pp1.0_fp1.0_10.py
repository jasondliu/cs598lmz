import types
# Test types.FunctionType
import unittest
class TestFunctionType(unittest.TestCase):
    def test_FunctionType(self):
        def f(x):
            return x


        def g(x):
            def h(y):
                return y


            return h(x)


        self.assertTrue(True, isinstance(f, types.FunctionType))
        self.assertTrue(True, isinstance(f, types.BuiltinFunctionType))
        self.assertTrue(True, isinstance(g, types.FunctionType))
        self.assertTrue(False, isinstance(g, types.BuiltinFunctionType))
        self.assertTrue(True, isinstance(str.upper, types.BuiltinMethodType))


def test_main():
    test.support.run_unittest(__name__)


if __name__ == '__main__':
    test_main()

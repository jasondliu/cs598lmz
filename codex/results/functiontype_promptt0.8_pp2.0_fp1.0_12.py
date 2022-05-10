import types
# Test types.FunctionType
#
# This is also an example of a test that needs cleanup, since it uses
# undocumented features of unittest.
#
from test.test_support import TESTFN, run_unittest
import unittest
from test.test_support import check_impl_detail
from types import FunctionType, LambdaType

class FunctionTestCase(unittest.TestCase):
    def test_functionattrs(self):
        # Test function attributes
        def f():
            """Hello"""
            pass

        self.assertEqual(f.__name__, "f")
        self.assertEqual(f.__doc__, "Hello")
        self.assertEqual(f.__dict__, {})
        self.assertEqual(f.__code__.co_nlocals, 0)
        self.assertEqual(f.__code__.co_stacksize, 2)

        def g(a, *b, **c):
            pass

        self.assertEqual(g.__code__.co_nlocals, 1)

        def h(

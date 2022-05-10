import types
# Test types.FunctionType with built-in functions (issue #6565)
import math
import unittest
try:
    cmp
except NameError:
    def cmp(a, b):
        return (a > b) - (a < b)
class TestFunctionType(unittest.TestCase):
    def test_str_function(self):
        s = None
        for x in (None, "123"):
            s = str(x)
            self.assertIs(type(s), str)
            self.assertEqual(s, "None" if x is None else "123")
        self.assertIs(s, str(None))
        self.assertIs(s, str("123"))
    def test_repr_function(self):
        for x in (1, 2.5, 1+2j):
            r = repr(x)
            self.assertIs(type(r), str)
            self.assertEqual(x, eval(r))
    def test_cmp_function(self):
        for x, y in ((1, 2), (2, 2

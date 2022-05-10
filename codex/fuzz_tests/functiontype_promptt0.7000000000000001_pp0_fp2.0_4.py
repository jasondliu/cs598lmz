import types
# Test types.FunctionType for user-defined functions
import unittest

# types.FunctionType() should accept any callable object
class FunctionTypeTest(unittest.TestCase):

    def setUp(self):
        self.f = lambda: 0

    def test_functiontype(self):
        new_f = types.FunctionType(self.f.__code__,
                                   self.f.__globals__,
                                   name=self.f.__name__,
                                   argdefs=self.f.__defaults__,
                                   closure=self.f.__closure__)
        self.assertTrue(callable(new_f))


class FunctionTypeCallTest(unittest.TestCase):

    def setUp(self):
        self.f = lambda: 0
        self.new_f = types.FunctionType(self.f.__code__,
                                        self.f.__globals__,
                                        name=self.f.__name__,
                                        argdefs=self.f.__defaults__,
                                        closure=self.f

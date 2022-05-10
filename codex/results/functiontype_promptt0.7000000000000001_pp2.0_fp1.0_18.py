import types
# Test types.FunctionType

import unittest

class FunctionTypeTestCase(unittest.TestCase):

    def test_function(self):
        def f(): pass
        self.assertTrue(
            isinstance(f, types.FunctionType)
        )

    def test_lambda(self):
        f = lambda: None
        self.assertTrue(
            isinstance(f, types.FunctionType)
        )

    def test_method(self):
        class Foo(object):
            def f(self): pass
        self.assertTrue(
            isinstance(Foo().f, types.FunctionType)
        )

    def test_constructor(self):
        class Foo(object):
            def __init__(self): pass
        self.assertTrue(
            isinstance(Foo.__init__, types.FunctionType)
        )

    def test_staticmethod(self):
        class Foo(object):
            @staticmethod
            def f(): pass
        self.assertTrue(
            isinstance(Foo.f, types.FunctionType)
        )

    def

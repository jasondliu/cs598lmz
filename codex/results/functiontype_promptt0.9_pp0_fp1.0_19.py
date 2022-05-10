import types
# Test types.FunctionType

import unittest
from test import test_support
from sys import getrefcount
import types, new

class FunctionTestCase(unittest.TestCase):
    def test_truth(self):
        self.assert_(not not new.function(lambda: None, {}))

    def test_call(self):
        import new
        global called
        called = 0
        def f(a):
            global called
            called = 1
        func = new.function(f.func_code, {}, None, None, (f.func_defaults or ()))
        func()
        self.assert_(called)

    def test_call_with_kwargs(self):
        import new
        global called
        called = 0
        def f(a):
            global called
            called = 1
        func = new.function(f.func_code, {}, None, None, (f.func_defaults or ()))
        func(a=1)
        self.assert_(called)

    def test_mapping_interface(self):
        def f(a): pass

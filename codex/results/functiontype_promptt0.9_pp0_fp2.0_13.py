import types
# Test types.FunctionType and types.MethodType
# types.MethodType doc is wrong!

def f(x):
    return x + 42

class C:
    def f(self, x):
        return x + self.x

import test.test_support, unittest

class TypesTests(unittest.TestCase):
    def test_no_args(self):
        self.assertEquals(f.__code__.co_argcount, 1)

    def test_varargs(self):
        def f(*args):
            pass
        self.assertEquals(f.__code__.co_flags & 0x04, 0x04)

        def g(arg, *args):
            pass
        self.assertEquals(g.__code__.co_flags & 0x04, 0x04)

    def test_varkeywords(self):
        def f(**kwargs):
            pass
        self.assertEquals(f.__code__.co_flags & 0x08, 0x08)

        def g(arg, **kwargs):
           

import types
# Test types.FunctionType and types.MethodType here
class Foo(object):
  def foo_method(self):
    pass
  def foo_callable(self):
    pass
  foo_callable = staticmethod(foo_callable)

import unittest
# Test isFunctionType, isMethodType, and isBuiltinFunctionOrMethod here
class MyTests(unittest.TestCase):
  def test_IsFunctionType(self):
    def foo():
      pass
    self.assertEqual(foo.__class__, types.FunctionType)

    foo_callable = types.MethodType(foo, Foo)
    self.assertEqual(foo_callable.__class__, types.MethodType)
    self.assertEqual(foo_callable.__func__, foo)
    self.assertEqual(foo_callable, Foo
        .foo_method.__get__(Foo()))

    foo_callable = types.MethodType(foo, Foo(), Foo)
    self.assertEqual(foo_callable.__class__, types.MethodType)


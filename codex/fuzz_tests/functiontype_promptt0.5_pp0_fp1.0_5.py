import types
# Test types.FunctionType
import sys
import unittest
from test import support

class Foo:
    def __init__(self, value):
        self.value = value

    def __call__(self):
        return self.value

class FunctionTestCase(unittest.TestCase):
    def test_basic_attributes(self):
        def f():
            """This is a test function."""
            pass

        self.assertEqual(f.__name__, 'f')
        self.assertEqual(f.__doc__, 'This is a test function.')
        self.assertEqual(f.__annotations__, {})
        self.assertEqual(f.__kwdefaults__, None)
        self.assertEqual(f.__defaults__, None)
        self.assertEqual(f.__code__.co_argcount, 0)
        self.assertEqual(f.__code__.co_kwonlyargcount, 0)
        self.assertFalse(f.__code__.co_flags & 0x08)
        self.

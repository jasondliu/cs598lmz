from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("i")
s.size

from array import array
a = array.__new__(array)
a.__init__("i")
a.itemsize

# -----------------------------------------------------------------------------
# Tests for new-style classes with __new__ and __init__
# -----------------------------------------------------------------------------

from test.test_support import run_unittest
import unittest

class NewInitTestCase(unittest.TestCase):
    def test_basic(self):
        class C(object):
            def __new__(cls, foo):
                self = object.__new__(cls)
                self.foo = foo
                return self
            def __init__(self, foo):
                pass
        self.assertEqual(C(42).foo, 42)
        self.assertRaises(TypeError, C)

    def test_basic_with_kwargs(self):
        class C(object):
            def __new__(cls, foo):
                self = object.__new__(cls)
                self.foo = foo
                return self

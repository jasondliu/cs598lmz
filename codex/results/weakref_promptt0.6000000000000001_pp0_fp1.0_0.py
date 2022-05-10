import weakref
# Test weakref.ref
from test import support
import unittest
from weakref import ref
import gc


class Foo:
    pass

class C:
    pass

class D(C):
    pass

class E(D):
    pass

class F(C):
    pass

class G(F, E):
    pass

class H(F, E):
    pass


class TestWeakref(unittest.TestCase):

    def test_basic(self):
        f = Foo()
        r = ref(f)
        self.assertEqual(r(), f)
        f = None
        gc.collect()
        self.assertEqual(r(), None)

    def test_callable(self):
        f = Foo()
        r = ref(f)
        self.assertEqual(callable(r), False)

    def test_newstyle(self):
        f = Foo()
        r = ref(f)
        self.assertEqual(isinstance(r, weakref.ReferenceType), True)

    def test_oldstyle(

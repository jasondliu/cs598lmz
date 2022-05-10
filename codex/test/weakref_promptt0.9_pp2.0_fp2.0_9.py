import weakref
# Test weakref.ref() with a custom class
import sys
from test.support import import_module
from test.support import captured_stderr
from test.support import check_warnings


class Foo:
    pass


class FooSub(Foo):
    pass


class BarBazz:
    pass


class TestWeakRef(unittest.TestCase):

    def test_ref_new_style_class(self):
        self.assertTrue(issubclass(weakref.ref, object))

    def test_instance_weak_ref(self):
        f = Foo()
        r = weakref.ref(f)
        self.assertEqual(r(), f)
        self.assertEqual(type(r), weakref.ReferenceType)

    def test_instance_weak_ref_ex(self):
        f = Foo()
        r = weakref.ref(f, lambda u: u)
        self.assertEqual(r(), f)
        self.assertEqual(type(r), weakref.ReferenceType)


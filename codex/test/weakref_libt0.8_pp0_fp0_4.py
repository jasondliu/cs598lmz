import weakref
import unittest

class Foo(object):
    def __init__(self): pass

class TestWeak(unittest.TestCase):
    def setUp(self):
        self.foo = Foo()

    def tearDown(self):
        self.foo = None

    def test_weak(self):
        wr = weakref.ref(self.foo)
        self.assertEqual(wr(), self.foo)
        del self.foo
        # now the weak reference should be dead
        self.assertEqual(wr(), None)

        # a weak reference to a local variable should not keep the object alive
        x = Foo()
        wr = weakref.ref(x)
        del x
        # now the weak reference should be dead
        self.assertEqual(wr(), None)

    def test_strong(self):
        wr = wr_strong = weakref.ref(self.foo)
        self.assertEqual(wr(), self.foo)
        self.assertEqual(wr_strong(), self.foo)
        del self.foo
        # now

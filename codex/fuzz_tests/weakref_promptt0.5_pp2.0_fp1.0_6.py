import weakref
# Test weakref.ref
import unittest
import gc

class TestWeakref(unittest.TestCase):

    def test_basic(self):
        o = object()
        r = weakref.ref(o)
        self.assertIs(r(), o)
        self.assertIs(weakref.getweakrefcount(o), 1)
        self.assertIs(weakref.getweakrefs(o), [r])
        self.assertIs(r(), o)
        o2 = r()
        self.assertIs(o2, o)
        o = None
        gc.collect()
        self.assertIs(r(), None)
        self.assertIs(o2, None)
        self.assertIs(weakref.getweakrefcount(o2), 0)
        self.assertIs(weakref.getweakrefs(o2), [])

    def test_callback(self):
        l = []
        def callback(arg):
            l.append(arg)
        o = object()
        r = weakref.ref(o, callback)
        self

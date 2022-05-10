import gc, weakref
import sys

#------------------------------------------------------------------------------

class TestWeakref(unittest.TestCase):

    def test_basic(self):
        class Foo:
            pass
        f = Foo()
        f.x = 42
        d = weakref.WeakValueDictionary()
        d[1] = f
        self.assertEqual(d[1].x, 42)
        del f
        gc.collect()
        self.assertEqual(len(d), 0)

    def test_basic_with_callback(self):
        class Foo:
            pass
        f = Foo()
        f.x = 42
        d = weakref.WeakValueDictionary()
        l = []
        def callback(arg):
            l.append(arg)
        d[1] = f
        r = weakref.ref(f, callback)
        self.assertEqual(d[1].x, 42)
        del f
        gc.collect()
        self.assertEqual(len(d), 0)
        self.assertEqual(len(l), 1)

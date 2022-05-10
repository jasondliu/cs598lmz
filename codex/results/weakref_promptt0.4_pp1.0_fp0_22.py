import weakref
# Test weakref.ref() on builtin types
import sys
import gc

class TestWeakRef:
    def f(self, arg):
        return lambda: arg

    def test_basic(self):
        a = 42
        b = "hello"
        c = 1.25
        d = [1, 2, 3]
        f = self.f(42)
        p = weakref.ref(a)
        q = weakref.ref(b)
        r = weakref.ref(c)
        s = weakref.ref(d)
        t = weakref.ref(f)
        for x in p, q, r, s, t:
            self.assertEqual(x(), x())
            self.assertEqual(type(x()), type(x()))
        del a, b, c, d, f
        gc.collect()
        for x in p, q, r, s, t:
            self.assertEqual(x(), x())
            self.assertEqual(type(x()), type(x()))

    def test_callable(

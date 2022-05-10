import weakref
# Test weakref.ref
class TestRef(unittest.TestCase):
    def testRef(self):
        W = weakref.ref
        class Foo:
            pass

        f = Foo()
        p = W(f)
        self.assertEqual(p(), f)
        del f
        self.assertEqual(p(), None)

    def testCallable(self):
        W = weakref.ref
        class Foo:
            def __call__(self):
                return 42
        f = Foo()
        p = W(f)
        self.assertEqual(p(), 42)
        self.assertEqual(p()(), 42)

    def testHash(self):
        W = weakref.ref
        class Foo:
            pass
        f = Foo()
        p = W(f)
        self.assertEqual(hash(p), hash(f))
        self.assertEqual(len(set([p, f])), 1)

    def testBool(self):
        W = weakref.ref
        class Foo:
            pass
        f = Foo

import weakref
# Test weakref.ref

class Foo(object):
    pass

def f():
    pass

class Test(unittest.TestCase):

    def test_basic(self):
        a = ['some sequence']
        self.assertEqual(weakref.ref(a), weakref.ref(a))
        b = a[:]
        self.assertNotEqual(weakref.ref(a), weakref.ref(b))

        class Foo(object): pass
        f = Foo()
        self.assertEqual(weakref.ref(f), weakref.ref(f))
        g = Foo()
        self.assertNotEqual(weakref.ref(f), weakref.ref(g))

        self.assertNotEqual(weakref.ref(lambda: None), weakref.ref(lambda: None))

    def test_hash(self):
        # refs must be hashable
        a = []
        ha = weakref.ref(a)
        dct = {}
        dct[ha] = 1
        self.assertEqual(dct[ha], 1)

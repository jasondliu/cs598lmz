import weakref
# Test weakref.ref instead of weakref.WeakKeyDictionary since weakref.WeakKeyDictionary
# does not support weakref.ref as hashable key.
@unittest.skipUnless(hasattr(weakref, 'ref'),
                     'requires weakref.ref')
class WeakKeyDictTestCase(unittest.TestCase):

    def test_basic(self):
        a = weakref.ref(A(42))
        b = weakref.ref(A(42))
        d = weakref.WeakKeyDictionary()
        d[a] = 42
        d[b] = 24
        self.assertEqual(d[a], 42)
        self.assertEqual(d[b], 24)
        self.assertEqual(set(d.items()), {(a, 42), (b, 24)})
        self.assertEqual(set(d.keys()), {a, b})
        self.assertEqual(d.pop(b), 24)
        del d[a]
        self.assertEqual(d.items(), [])

    def test_mut

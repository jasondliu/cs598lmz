import gc, weakref

class TestWeakref(unittest.TestCase):

    def test_basic(self):
        # Test basic weakref operations.
        # Test by creating a cycle:  a -> b -> a
        a = TestWeakref.A()
        a.b = TestWeakref.B(a)
        wr = weakref.ref(a)
        self.assertEqual(wr(), a)
        self.assertEqual(wr().b.a(), a)
        self.assertEqual(wr().b.a().b.a(), a)
        self.assertEqual(wr().b.a().b.a().b.a(), a)
        del a
        self.assertEqual(wr(), None)
        self.assertRaises(ReferenceError, getattr, wr(), 'b')
        self.assertRaises(ReferenceError, getattr, wr(), 'b')
        self.assertRaises(ReferenceError, getattr, wr(), 'b')

    def test_callbacks(self):
        # Test proper invocation of callbacks
        l = []
        def callback

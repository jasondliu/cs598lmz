import weakref
# Test weakref.ref()
import _weakref


class TestWeakref:

    def test_ref_basic(self):
        self.assertRaises(TypeError, _weakref.ref)
        self.assertRaises(TypeError, _weakref.ref, 42, 42)
        def f(): pass
        r = _weakref.ref(f)
        self.assertEqual(r(), f)
        self.assertEqual(r.__call__(), f)
        self.assertEqual(r.__call__(), f())

    def test_callable_ref(self):
        def callback(arg):
            self.assertEqual(arg(), obj)
            self.callback_called = True
        self.callback_called = False
        obj = []
        ref = _weakref.ref(obj, callback)
        self.assertIsInstance(ref, weakref.CallableRefType)
        del obj
        support.gc_collect()
        self.assertTrue(self.callback_called)
        self.assertEqual(ref(), None)

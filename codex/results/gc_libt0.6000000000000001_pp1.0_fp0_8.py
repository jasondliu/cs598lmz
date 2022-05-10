import gc, weakref
+from .support import gc_collect
+
+class Foo(object):
+    pass
+
+class TestWeakRef(unittest.TestCase):
+
+    def test_callback(self):
+        l = []
+        def callback(arg):
+            l.append(arg)
+        o = Foo()
+        o.x = 42
+        w = weakref.ref(o, callback)
+        self.assertEqual(w(), o)
+        self.assertEqual(w().x, 42)
+        del o
+        gc_collect()
+        self.assertEqual(len(l), 1)
+        self.assertEqual(l[0](), w())
+        self.assertEqual(l[0]().x, 42)
+        self.assert_(w() is None)
+        self.assertEqual(len(l), 1)
+
+    def test_callback_with_exception(self):
+        def badcallback(arg):
+            raise Exception
+        o

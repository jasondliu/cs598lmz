import weakref
+from functools import partial
+
+import pytest
+
+
+class TestWeakref:
+    def test_weakref_callback(self):
+        x = []
+        callback = partial(x.append, 'callback')
+        w = weakref.ref(1, callback)
+        assert w() == 1
+        assert x == []
+
+        del w
+        assert x == ['callback']
+
+    def test_weakref_callback_ref(self):
+        x = []
+        callback = partial(x.append, 'callback')
+        w = weakref.ref(1, callback)
+        wr = weakref.ref(w)
+        assert wr() == w
+        assert x == []
+
+        del w
+        assert wr() is None
+        assert x == []
+
+        del wr
+        assert x == ['callback']
+
+    def test_weakref_callback_gc(self):
+        x = []
+        callback = partial(x.append, '

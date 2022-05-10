import gc, weakref
+from weakref import ref as weakref_ref
+
+
+def test_weakref_ref():
+    ref = weakref_ref(2)
+    assert ref() == 2
+    del ref
+    assert gc.collect() == 0
+
+
+def test_weakref_ref_with_callback():
+    def callback(ref):
+        callback.called = True
+    ref = weakref_ref(2, callback)
+    assert ref() == 2
+    del ref
+    assert gc.collect() == 1
+    assert callback.called
+
+
+def test_weakref_proxy():
+    ref = weakref_ref(2)
+    proxy = ref.proxy()
+    assert proxy == 2
+    del ref
+    assert gc.collect() == 0
+    assert proxy == 2
+    del proxy
+    assert gc.collect() == 0
+
+
+def test_weakref_proxy_with_callback():
+    def callback(ref):
+        callback.called =

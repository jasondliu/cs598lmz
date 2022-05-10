import gc, weakref
+
+
+a = [1, 2, 3]
+b = [4, 5, 6]
+
+a.append(b)
+b.append(a)
+
+print(a)
+print(b)
+
+print(gc.collect())
+print(gc.get_referrers(a))
+print(gc.get_referrers(b))
+
+
+obj = object()
+w = weakref.ref(obj)
+
+print(obj)
+print(w())
+
+obj = None
+
+print(w())
+
+print(gc.collect())
+print(w())
+
+
+obj = object()
+w = weakref.ref(obj)
+
+print(obj)
+print(w())
+
+obj = None
+
+print(w())
+
+print(gc.collect())
+print(w())


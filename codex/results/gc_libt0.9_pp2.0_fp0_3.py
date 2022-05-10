import gc, weakref, abc
+
+
+class C(object):
+	pass
+obj = C()
+r = weakref.ref(obj)
+gc.collect()
+assert r() is obj
+del obj
+gc.collect()
+print('before: r is {}'.format(r))
+C.__dict__.clear()
+gc.collect()
+
+print('after: r is {}'.format(r))
+assert r() is None
+print("Done")


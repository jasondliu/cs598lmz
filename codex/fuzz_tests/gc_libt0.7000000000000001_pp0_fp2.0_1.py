import gc, weakref
+
+
+class A:
+    def __init__(self, value):
+        self.value = value
+    def __repr__(self):
+        return str(self.value)
+
+a = A(10)
+d = weakref.WeakValueDictionary()
+d['primary'] = a
+d['primary']
+d
+print(d)
+del a
+d # as a is deleted, it is not available
+gc.collect()
+d # as a is deleted, it is not available
+
+
+a = A(10)
+d = weakref.WeakKeyDictionary()
+d[a] = "test"
+d
+a2 = A(15)
+d[a2] = "test2"
+d
+del a
+d # as a is deleted, it is not available
+gc.collect()
+d # as a is deleted, it is not available
+
+
+
+
+
+
+
+
+
+
+
+
+


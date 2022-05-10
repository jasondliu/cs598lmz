import gc, weakref
+from objgraph import show_most_common_types
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
+print('d["primary"]', d['primary'])
+del a
+gc.collect()
+print('d["primary"]', d['primary'])
+
+def f():
+    a = [A(i) for i in range(10)]
+    d = weakref.WeakValueDictionary()
+    d['primary'] = a
+    print('d["primary"]', d['primary'])
+    del a
+    gc.collect()
+    print('d["primary"]', d['primary'])
+
+f()
+
+s = 'string'
+d = weakref.WeakKeyDictionary()
+d[s] = 'value'

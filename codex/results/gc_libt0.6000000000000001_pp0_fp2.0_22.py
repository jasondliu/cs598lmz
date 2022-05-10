import gc, weakref
+
+class A(object):
+    def __init__(self, value):
+        self.value = value
+    def __repr__(self):
+        return str(self.value)
+
+a = A(10)
+d = weakref.WeakValueDictionary()
+d['primary'] = a
+print(d['primary'])
+del a
+gc.collect()
+print(d['primary'])
+
+def callback(reference):
+    print('callback(', reference, ')')
+
+a = A(10)
+d = weakref.WeakValueDictionary()
+d['primary'] = a
+r = weakref.ref(a, callback)
+print('deleting a')
+del a
+print('collecting')
+gc.collect()
+print('done')
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

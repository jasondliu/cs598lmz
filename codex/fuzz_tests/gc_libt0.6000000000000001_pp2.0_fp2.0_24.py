import gc, weakref, inspect
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
+
+print 'Before:'
+print d.items()
+a = None
+gc.collect()
+print 'After:'
+print d.items()
+
+
+# import gc
+# class A:
+#     def __init__(self, value):
+#         self.value = value
+#     def __repr__(self):
+#         return str(self.value)
+#
+# a = A(10)
+# d = {}
+# d[1] = a
+# d[2] = weakref.ref(a)
+#
+# print 'Before:'
+# print d.items()
+# print d[1], d[2]()
+

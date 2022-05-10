import gc, weakref
+
+class Foo(object):
+    def __init__(self, name):
+        self.name = name
+
+    def __del__(self):
+        print 'Bye %s' % self.name
+
+obj = Foo('obj')
+r = weakref.ref(obj)
+print r
+
+print obj
+obj = None
+print obj
+print r()
+print r
+
+gc.collect()
+print r()
+
+print '-' * 30
+
+class Foo(object):
+    def __init__(self, name):
+        self.name = name
+
+    def __del__(self):
+        print 'Bye %s' % self.name
+
+obj = Foo('obj')
+r = weakref.ref(obj)
+print r
+
+print obj
+obj = None
+print obj
+print r()
+print r
+
+# gc.collect()
+print r()


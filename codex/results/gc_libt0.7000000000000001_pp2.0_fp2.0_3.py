import gc, weakref
+
+# How to create a weak-reference to an object in Python
+
+# create a weak-reference to an object
+# weakref.ref(myobj)
+
+# For example:
+
+
+class C:
+    def __init__(self, name):
+        self.name = name
+
+    def __del__(self):
+        print('__del__ called for %s' % self)
+
+    def __repr__(self):
+        return self.name
+
+
+a = C('a')
+b = C('b')
+
+print('a:', a)
+print('b:', b)
+
+# create weak reference to object 'a'
+a_weak = weakref.ref(a)
+
+print('a_weak:', a_weak)
+print('a_weak()', a_weak())
+
+
+# mark 'a' as eligible for garbage collection
+del a
+
+print('\ndelete a:')
+print

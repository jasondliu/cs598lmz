import gc, weakref
+
+gc.set_debug(gc.DEBUG_LEAK) # or gc.DEBUG_SAVEALL
+
+class C(object): pass
+
+class B(object):
+    def __init__(self, value):
+        self.value = value
+
+    def __del__(self):
+        print 'deleting', self
+
+
+class A(object):
+    def __init__(self):
+        self.b = B(10)
+
+    def __del__(self):
+        print 'deleting', self
+
+a = A()
+del A
+
+
+# Get refs to all old objects.
+old_objects = gc.get_objects()
+
+# Run a full collection.
+gc.collect()
+
+# Get refs to all new objects.
+new_objects = gc.get_objects()
+
+# Get the difference.
+for obj in new_objects:
+    if obj not in old_objects:
+

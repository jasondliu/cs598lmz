import gc, weakref
+
+
+class WeakMethod(object):
+    def __init__(self, func):
+        self.func = func.im_func
+        self.cls = func.im_class
+        self.object = weakref.ref(func.im_self)
+
+    def __call__(self):
+        obj = self.object()
+        if obj is not None:
+            return self.func.__get__(obj, self.cls)
+        raise ReferenceError
+
+    def __eq__(self, other):
+        return self.func == other.func and self.cls == other.cls
+
+    def __hash__(self):
+        return hash((self.func, self.cls))
+
+
+class WeakMethodBound(object):
+    """
+    This class is used to keep a weak reference to a bound method.
+    """
+    def __init__(self, func):
+        self.func = func.im_func
+        self.object = weakref

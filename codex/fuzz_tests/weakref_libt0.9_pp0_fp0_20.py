import weakref
+
+
+class WeakMethod(object):
+    """Weak reference proxy to a bound method (aka. function), with
+    a replacement function.
+
+    Args:
+        method (bound method): A bound method, which we want to
+            create a weak version of.
+        subsitute (function): A function to call if the original
+            function has been garbage collected.
+
+    Attributes:
+        is_dead (bool): Is the original method dead (i.e. has been
+            garbage collected already)?
+
+    """
+
+    def __init__(self, method, subsitute):
+        self.function = getattr(method, "__func__", method)
+        try:
+            self.object = weakref.ref(method.__self__)
+        except TypeError:
+            self.object = None
+        self.subsitute = subsitute
+        self.is_dead = False
+
+    @property
+    def is_dead(self):
+        return self._is_dead

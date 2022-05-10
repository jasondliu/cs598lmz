import weakref
+import ctypes
+from functools import update_wrapper
+
+if sys.version_info[0] >= 3:
+    long = int
+    basestring = str
+
+
+def proxy(func):
+    """
+    Decorator to create proxies for instance methods. Useful if there is
+    code that uses the bound method directly and updating that code is not
+    an option.
+    """
+
+    def inner(self, *args, **kwargs):
+        return func(self._obj(), *args, **kwargs)
+
+    return update_wrapper(inner, func)
+
+
+class Proxy(object):
+    """
+    Baseclass for proxy classes.
+    """
+
+    __slots__ = ['_obj']
+
+    def __init__(self, obj):
+        object.__setattr__(self, '_obj', obj)
+
+    def __getattribute__(self, name):
+        if name == '_obj':
+            return object

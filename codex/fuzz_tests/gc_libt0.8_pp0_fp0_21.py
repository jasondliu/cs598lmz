import gc, weakref
+
+#
+# Module variables
+#
+
+_repr_instance_cache = weakref.WeakKeyDictionary()
+
+def _get_repr_instance(obj):
+    # Lookup existing represenation instance
+    try:
+        r = _repr_instance_cache[obj]
+    except KeyError:
+        # Create new represenation instance
+        r = _repr_instance_cache[obj] = _repr_instance(obj)
+    return r
+
+#
+# Classes
+#
+
+class _repr_instance(tuple):
+    """
+    An instance of this class contains the representation of an object (the
+    result of repr(obj)).  It also contains a reference to the object itself.
+    When the object dies, the representation is removed from the instance
+    cache.  This is done in a __del__() method, so garbage collection is not
+    enabled.
+    """
+
+    def __new__(cls, obj):


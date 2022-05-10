import weakref
+
+
+def _object_deleted(weak_pointer):
+    """Called when an object has been deleted.
+
+    The weak_pointer is the proxy that is being called.
+    The original object is gone already.
+
+    """
+    if weak_pointer.type == WeakProxy:
+        weak_pointer._proxytype = WeakProxy.DEAD
+    elif weak_pointer.type == WeakSubProxy:
+        weak_pointer._proxytype = WeakSubProxy.DEAD
+    else:
+        raise ValueError("Illegal weak pointer type: %r" % type(weak_pointer))
+
+
+class WeakProxy(object):
+    """A weak reference to an object that can call the referenced
+    object's methods.
+
+    """
+    ALIVE = 1
+    DEAD = 2
+
+    def __init__(self, object_, *methods):
+        """Create a new weak pointer.
+
+        object_ - the object to weak reference
+        methods - a list of methods that

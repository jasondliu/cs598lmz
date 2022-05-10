import weakref
+
+
+#
+# Callback assigner
+#
+
+class _CallbackAssigner:
+  """Assign a callback to an object.
+
+  This class allows assigning a callback to an object.  It uses a
+  weak reference to avoid having a circular reference.
+
+  """
+
+  def __init__(self, callback):
+    """Construct the callback assigner.
+
+    Parameters:
+
+      callback: The callback to assign to objects.
+
+    """
+    self._callback = callback
+    self._widgets = {}
+
+  def __get__(self, obj, cls):
+    """Return this instance.
+
+    For use in a descriptor.
+
+    """
+    if obj is None:
+      return self
+
+    elif obj not in self._widgets:
+      widget = self._callback(obj)
+      self._widgets[weakref.ref(obj)] = widget
+
+    else:
+      widget =

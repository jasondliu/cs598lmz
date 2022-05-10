import gc, weakref
+
+__all__ = ["BasicTracker", "EasyTracker"]
+
+
+class BasicTracker(object):
+    def __init__(self):
+        self._tracked = []
+
+    def clear(self) -> None:
+        self._tracked = []
+
+    def exclude(self, *items) -> None:
+        for item in items:
+            self._tracked.remove(item)
+
+    def track(self, *items) -> None:
+        for item in items:
+            self._tracked.append(item)
+
+    def __enter__(self):
+        return self
+
+    def __exit__(self, exc_type, exc_val, exc_tb):
+        self.clear()
+
+
+class EasyTracker(BasicTracker):
+    def __init__(self):
+        super().__init__()
+        self._tracked_refs: List[weakref.ref] = []
+        self._cleared = False
+
+

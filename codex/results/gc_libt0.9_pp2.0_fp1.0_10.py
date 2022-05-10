import gc, weakref, uuid
+from pyglet import gl, graphics, event
+from pyglet.window import key
+from pyglet.window import mouse
+from math import ceil, floor
+from . import resman
+from .util import *
+
+def _remove_if_exists(all, component):
+    all_tuple = list(all)
+    for c in all_tuple:
+        if weakref.ref(c) == weakref.ref(component):
+            all.remove(c)
+            break
+
+def _add_if_does_not_exist(all, component):
+    for c in all:
+        if weakref.ref(c) == weakref.ref(component):
+            return
+    all.append(component)
+
+class Signal:
+    def __init__(self):
+        self.handlers = set()
+
+    def handle(self, handler):
+        self.handlers.add(handler)
+        return self
+
+    def unhandle(

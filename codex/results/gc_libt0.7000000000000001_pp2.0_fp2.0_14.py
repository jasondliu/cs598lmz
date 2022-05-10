import gc, weakref
+from collections import defaultdict
+from contextlib import contextmanager
+from typing import *
+from time import time
+
+
+class TimeoutException(Exception):
+    pass
+
+
+class RunOutException(Exception):
+    pass
+
+
+class ResourceError(Exception):
+    pass
+
+
+class Pool:
+    def __init__(self, timeout: float = None):
+        self.timeout = timeout
+        self.resource_cls = None
+        self.resource_args = []
+        self.resource_kwargs = {}
+        self.resources: List[weakref.ref] = []
+        self.available_resources: List[weakref.ref] = []
+        self.unavailable_resources: Dict[Any, time] = {}
+
+    def __del__(self):
+        for resource in self.resources:
+            del resource
+        self.resources.clear()
+        self.available_resources.clear()
+        self.unavailable_resources.clear()


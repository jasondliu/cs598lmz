import gc, weakref
+from itertools import chain
+from collections import defaultdict
+
+
+def get_all_subclasses(cls):
+    """
+    Return all subclasses of class cls.
+    """
+    return cls.__subclasses__() + [g for s in cls.__subclasses__()
+                                   for g in get_all_subclasses(s)]
+
+
+def collect_all_subclasses(cls):
+    """
+    Return all subclasses of class cls, including cls itself.
+    """
+    return [cls] + get_all_subclasses(cls)
+
+
+def get_all_instances(cls):
+    """
+    Return all instances of class cls.
+    """
+    return [obj for obj in gc.get_objects()
+            if isinstance(obj, cls)]
+
+
+def collect_all_instances(cls):
+    """
+    Return all instances of class cls, including instances of sub

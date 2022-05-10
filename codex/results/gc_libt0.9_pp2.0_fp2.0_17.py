import gc, weakref, functools, pdb, operator
+
+def get_all_objects():
+    """
+    return all python objects that have been created
+    """
+    return gc.get_objects()
+
+def object_by_id(obj_id):
+    try:
+        for obj in get_all_objects():
+            if id(obj) == obj_id:
+                return obj
+        return None
+    except:
+        return None
+
+def all_references(obj_id):
+    try:
+        return gc.get_referrers(object_by_id(obj_id))
+    except:
+        return []
+
+def is_referenced(obj_id):
+    """
+    Returns whether or not the object is still referenced by something.
+    """
+    return bool(all_references(obj_id))
+
+def all_back_references(obj_id):
+    try:
+        return gc.get_referents(object

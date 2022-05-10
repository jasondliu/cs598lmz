import weakref
+
+
+class JsonFileStruct(object):
+    """
+    Json class
+
+    """
+
+    def __init__(self, name, **kwargs):
+        self._file_name = name
+        self._file_ref = None
+        self._cache = {}
+        self._lock = RLock()
+        self._ref_to_self = weakref.ref(self)
+
+    def _open(self, flag):
+        if self._file_ref is None:
+            self._file_ref = open(self._file_name, flag)
+        return self._file_ref
+
+    def _close(self):
+        # several improvements can be done here:
+        # 1: lock the cache while reading values.
+        # 2: use a weakref to store the file reference and this way
+        #    let pythons garbage collection do the work
+        self._file_ref.close()
+        self._file_ref = None
+
+    def _create_json

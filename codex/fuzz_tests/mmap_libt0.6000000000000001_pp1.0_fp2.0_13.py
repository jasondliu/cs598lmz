import mmap
+import sys
+
+class MemoryMap:
+    def __init__(self, file_name):
+        self.file_name = file_name
+        self.file = None
+        self.data = None
+
+    def __enter__(self):
+        self.file = open(self.file_name, "r+")
+        self.data = mmap.mmap(self.file.fileno(), 0)
+        return self
+
+    def __exit__(self, exc_type, exc_value, exc_tb):
+        self.data.close()
+        self.file.close()
+
+    def find(self, pattern, nth):
+        for i in range(nth):
+            self.data.seek(0)
+            offset = self.data.find(pattern)
+            if offset == -1:
+                return -1
+            self.data.seek(offset + 1)
+        return offset
+
+    def replace(self, pattern, replacement):
+       

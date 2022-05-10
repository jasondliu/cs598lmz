import mmap
+import datetime
+
+
+class mmap_file(object):
+    def __init__(self, filename, mode='r'):
+        self.filename = filename
+        self.mode = mode
+        self.file = None
+        self.mmap = None
+        self.n = 0
+
+    def __enter__(self):
+        self.file = open(self.filename, self.mode)
+        self.mmap = mmap.mmap(self.file.fileno(), 0, prot=mmap.PROT_READ)
+        return self
+
+    def __iter__(self):
+        return self
+
+    def __next__(self):
+        line = self.mmap.readline()
+        if not line:
+            raise StopIteration
+        self.n += 1
+        return line.decode()
+
+    def __exit__(self, *_):
+        self.mmap.close()
+        self.file.close()
+
+

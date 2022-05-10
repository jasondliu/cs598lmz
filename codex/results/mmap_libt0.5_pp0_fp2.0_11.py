import mmap
+
+class Mmap_file(object):
+    def __init__(self, filename, mode=mmap.ACCESS_WRITE, size=0):
+        self.size = size
+        self.filename = filename
+        self.mode = mode
+        self.file = open(filename, 'r+b')
+        self.mmap = mmap.mmap(self.file.fileno(), self.size)
+
+    def __del__(self):
+        self.mmap.close()
+        self.file.close()
+
+    def __len__(self):
+        return self.size
+
+    def __getitem__(self, key):
+        return self.mmap[key]
+
+    def __setitem__(self, key, value):
+        self.mmap[key] = value
+
+    def __getslice__(self, start, end):
+        return self.mmap[start:end]
+
+    def __setslice__(self, start

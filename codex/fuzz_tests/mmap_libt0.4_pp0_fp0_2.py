import mmap
+import struct
+
+
+class Mmap(object):
+    def __init__(self, filename, size):
+        self.filename = filename
+        self.size = size
+        self.mm = None
+        self.fd = None
+        self.offset = 0
+
+    def open(self):
+        self.fd = os.open(self.filename, os.O_RDWR | os.O_CREAT)
+        self.mm = mmap.mmap(self.fd, self.size)
+
+    def close(self):
+        self.mm.close()
+        os.close(self.fd)
+
+    def read(self, size):
+        data = self.mm[self.offset:self.offset + size]
+        self.offset += size
+        return data
+
+    def write(self, data):
+        self.mm[self.offset:self.offset + len(data)] = data
+        self.offset += len(data)
+
+    def seek

import mmap
+import time
+
+
+class MMap(object):
+
+    def __init__(self, filename, offset, size):
+        self.filename = filename
+        self.offset = offset
+        self.size = size
+        self.fd = os.open(filename, os.O_RDWR)
+        self.mm = mmap.mmap(self.fd, size, mmap.MAP_SHARED, mmap.PROT_WRITE)
+
+    def __del__(self):
+        self.mm.close()
+        os.close(self.fd)
+
+    def read(self):
+        self.mm.seek(self.offset)
+        return self.mm.read(self.size)
+
+    def write(self, data):
+        self.mm.seek(self.offset)
+        return self.mm.write(data)
+
+
+def main():
+    mmap = MMap('test.txt', 0, 1024)
+    while True:
+

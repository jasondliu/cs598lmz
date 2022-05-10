import mmap
+
+
+class mmap:
+    def __init__(self, filename, access=ACCESS_READ, tagname="", size=0):
+        self.tagname = tagname
+        if access == ACCESS_WRITE:
+            self.mode = 'w+'
+        else:
+            self.mode = 'r'
+
+        if size:
+            self.size = size
+        else:
+            self.size = os.stat(filename).st_size
+
+        self.file = open(filename, self.mode)
+        self.mm = mmap.mmap(self.file.fileno(), self.size, access=mmap.ACCESS_WRITE)
+
+    def close(self):
+        self.mm.close()
+        self.file.close()
+
+    def get_int(self, offset=0, size=4):
+        data = self.mm[offset:offset + size]
+        return struct.unpack('i', data)
+
+   

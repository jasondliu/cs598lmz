import mmap
+import struct
+
+class Tpv(object):
+    def __init__(self, file_name):
+        self.file_name = file_name
+        self.file = open(file_name, 'rb')
+        self.map = mmap.mmap(self.file.fileno(), 0, access=mmap.ACCESS_READ)
+        self.width = self.read_width()
+        self.height = self.read_height()
+        self.data = self.read_data()
+
+    def read_width(self):
+        return struct.unpack('<i', self.map[0:4])[0]
+
+    def read_height(self):
+        return struct.unpack('<i', self.map[4:8])[0]
+
+    def read_data(self):
+        return self.map[8:]
+
+    def __getitem__(self, key):
+        if isinstance(key, slice):
+            return self.data[key

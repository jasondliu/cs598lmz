import mmap
+import struct
+import sys
+
+
+class PcapReader:
+    def __init__(self, filename):
+        self.filename = filename
+        self.file = open(filename, 'rb')
+        self.mmap = mmap.mmap(self.file.fileno(), 0, prot=mmap.PROT_READ)
+
+    def __enter__(self):
+        return self
+
+    def __exit__(self, type, value, traceback):
+        self.mmap.close()
+        self.file.close()
+
+    def read_packet(self):
+        if self.mmap.tell() == len(self.mmap):
+            return None
+
+        header = self.mmap.read(16)
+        ts_sec, ts_usec, incl_len, orig_len = struct.unpack('IIII', header)
+
+        return self.mmap.read(incl_len)
+
+
+def main():
+    if

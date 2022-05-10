import mmap
+import struct
+import sys
+
+class KBitMap:
+    def __init__(self, size):
+        self.size = size
+        self._map = mmap.mmap(-1, size, mmap.MAP_PRIVATE | mmap.MAP_ANON, mmap.PROT_WRITE | mmap.PROT_READ)
+
+    def __getitem__(self, i):
+        index = i // 8
+        offset = i % 8
+        if index >= self.size:
+            raise IndexError("index out of bound")
+        return (ord(self._map[index]) >> offset) & 1
+
+    def __setitem__(self, i, v):
+        index = i // 8
+        offset = i % 8
+        if index >= self.size:
+            raise IndexError("index out of bound")
+        if v & 1 == 0:
+            self._map[index] = chr(ord(self._map[index]) & ~(1 << offset))
+       

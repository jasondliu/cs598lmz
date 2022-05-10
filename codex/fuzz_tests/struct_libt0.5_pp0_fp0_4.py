import _struct
+
+
+class Buffer(object):
+    def __init__(self, buf=None):
+        if buf is None:
+            self.buf = bytearray()
+        else:
+            self.buf = bytearray(buf)
+
+    def write(self, data):
+        self.buf += data
+
+    def read(self, length):
+        data = self.buf[:length]
+        self.buf = self.buf[length:]
+        return data
+
+    def readall(self):
+        return self.read(len(self.buf))
+
+    def readline(self, size=-1):
+        i = self.buf.find(b'\n')
+        if i < 0:
+            i = len(self.buf)
+        else:
+            i += 1
+        if size >= 0 and i > size:
+            i = size
+        data = self.read(i)
+        return data
+
+    def readlines(

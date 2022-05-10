import _struct
+
+class LittleNibble(bytearray):
+    def __new__(self, data):
+        return super(LittleNibble, self).__new__(self, data)
+
+    def __init__(self, data):
+        data = bytes(data)
+        self.byte = 0
+        self.n = 0
+        super(LittleNibble, self).__init__(data)
+
+    def __iter__(self):
+        return self
+
+    def __next__(self):
+        if self.n == 0:
+            if len(self) > 0:
+                self.byte = self.pop(0)
+            else:
+                raise StopIteration
+        ret = self.byte & 0x0f
+        self.byte >>= 4
+        self.n = (self.n + 1) % 2
+        return ret
+
+    def pop(self):
+        return next(self)
+
+if __name__ == "__main__":
+   

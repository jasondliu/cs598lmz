import _struct
+
+class C_BinaryReader:
+    def __init__(self, file):
+        self.file = file
+        self.file.seek(0, 2)
+        self.fileSize = self.file.tell()
+        self.file.seek(0, 0)
+
+    def get_struct(self, format):
+        return _struct.unpack(format, self.file.read(8))
+
+    def get_bytes(self, count):
+        return self.file.read(count)
+
+    def get_string(self, count):
+        return self.file.read(count).decode('utf-8')
+
+    def get_byte(self):
+        return self.get_struct('B')[0]
+
+    def get_word(self):
+        return self.get_struct('H')[0]
+
+    def get_dword(self):
+        return self.get_struct('I')[0]
+
+    def get_q

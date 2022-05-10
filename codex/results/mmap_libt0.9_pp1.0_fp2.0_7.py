import mmap
+
+
+class MmapWrapper:
+
+    def __init__(self, map_file):
+        self.my_file = map_file
+        self.data_file = open(map_file, "r+b")
+        self.size = os.stat(map_file).st_size
+        self.map_data = mmap.mmap(self.data_file.fileno(), self.size)
+
+    def write_data(self, name, data):
+        self.map_data.seek(0)
+        if data is not None:
+            string_to_write = name + " : " + data + "\n"
+            self.map_data.write(string_to_write.encode())
+        else:
+            self.map_data.write("".encode())
+
+    def read_file_head(self):
+        self.map_data.seek(0)
+        print(self.map_data.readline())


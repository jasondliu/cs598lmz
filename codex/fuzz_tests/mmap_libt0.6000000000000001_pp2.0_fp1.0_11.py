import mmap
+import re
+
+def read_file(filename):
+    with open(filename, "r") as f:
+        return mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
+
+def get_num_lines(filename):
+    with open(filename, "r") as f:
+        return sum(1 for line in f)
+
+# def read_file(filename):
+#     with open(filename, "r") as f:
+#         return f.read()
+
+# def get_num_lines(filename):
+#     with open(filename, "r") as f:
+#         return len(f.readlines())
+
+def main():
+    import sys
+    filename = sys.argv[1]
+    text = read_file(filename)
+    text_length = len(text)
+    num_lines = get_num_lines(filename)
+    print("File is %d bytes long" % text_length)
+    print("

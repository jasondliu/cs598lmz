import mmap
+
+
+def get_file_lines(file_name):
+    with open(file_name, 'r') as f:
+        return mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ).readlines()
+
+
+def get_file_words(file_name):
+    with open(file_name, 'r') as f:
+        return mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ).read().split()
+
+
+def get_file_chars(file_name):
+    with open(file_name, 'r') as f:
+        return mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ).read().replace('\n', '')
+
+
+def get_file_size(file_name):
+    return os.path.getsize(file_name)
+
+
+def get_file_stats(file_name):
+    return {
+        '

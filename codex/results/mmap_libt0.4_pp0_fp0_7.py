import mmap
+import re
+
+def find_pattern(pattern, filename):
+    with open(filename, 'r') as f:
+        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
+        index = 0
+        while True:
+            index = s.find(pattern, index)
+            if index == -1:
+                break
+            yield index
+            index += 1
+
+def find_pattern_re(pattern, filename):
+    with open(filename, 'r') as f:
+        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
+        for match in re.finditer(pattern, s):
+            yield match.start()
+
+def main():
+    pattern = 'def'
+    filename = 'mmap_example.py'
+    for match in find_pattern_re(pattern, filename):
+        print match
+
+if __name__ == '__main__':
+    main

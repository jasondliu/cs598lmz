import mmap
+
+def find(pattern, file):
+    with open(file, 'rb') as f:
+        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
+        i = s.find(pattern)
+        while i != -1:
+            print i
+            i = s.find(pattern, i+1)
+            break
+
+find("12345", "test.txt")


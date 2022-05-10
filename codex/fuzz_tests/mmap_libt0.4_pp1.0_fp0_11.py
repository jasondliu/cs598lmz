import mmap
+import sys
+import os
+
+
+def main():
+    if len(sys.argv) < 2:
+        print("Usage: %s <file>" % sys.argv[0])
+        sys.exit(1)
+
+    filename = sys.argv[1]
+
+    if not os.path.exists(filename):
+        print("File %s does not exist!" % filename)
+        sys.exit(1)
+
+    if not os.path.isfile(filename):
+        print("%s is not a file!" % filename)
+        sys.exit(1)
+
+    if not os.access(filename, os.R_OK):
+        print("File %s is not readable!" % filename)
+        sys.exit(1)
+
+    file_size = os.path.getsize(filename)
+
+    with open(filename, "rb") as f:
+        mm = mmap.mmap(f.fileno(), 0, access=mmap.ACC

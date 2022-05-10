import mmap
+import os
+import re
+import sys
+
+def main():
+    if len(sys.argv) < 2:
+        print("Usage: %s <file>" % sys.argv[0])
+        sys.exit(1)
+
+    fd = os.open(sys.argv[1], os.O_RDONLY)
+    m = mmap.mmap(fd, 0, prot=mmap.PROT_READ)
+    os.close(fd)
+
+    for line in m:
+        if re.search("^\s*$", line):
+            continue
+        if re.search("^\s*\#", line):
+            continue
+        if re.search("^\s*\[", line):
+            continue
+
+        print(line)
+
+if __name__ == "__main__":
+    main()


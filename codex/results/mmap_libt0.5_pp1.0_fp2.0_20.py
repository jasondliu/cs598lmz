import mmap
+import os
+import sys
+
+
+def usage():
+    print("usage: " + sys.argv[0] + " <file>")
+
+
+def main():
+    if len(sys.argv) != 2:
+        usage()
+        sys.exit(1)
+
+    filename = sys.argv[1]
+    if not os.path.isfile(filename):
+        print("file not found: {0}".format(filename))
+        sys.exit(1)
+
+    with open(filename, "rb") as f:
+        mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
+        data = mm.read()
+        mm.close()
+        f.close()
+
+    print(data)
+
+
+if __name__ == "__main__":
+    main()


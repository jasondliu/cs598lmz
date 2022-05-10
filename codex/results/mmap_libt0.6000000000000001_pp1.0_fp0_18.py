import mmap
+import subprocess
+import sys
+
+def main():
+    if len(sys.argv) < 2:
+        print("Usage: {} <file>".format(sys.argv[0]))
+        sys.exit(1)
+
+    f = open(sys.argv[1])
+    m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
+    n = 0
+    for line in iter(m.readline, ""):
+        if n == 0:
+            n += 1
+            continue
+        n += 1
+        print("{} {}".format(n, line.split(',')[1]))
+        if n == 10:
+            break
+    m.close()
+
+if __name__ == '__main__':
+    main()


import mmap
+import sys
+import os
+
+
+def main():
+    random_data = os.urandom(1024 * 1024 * 1024 * 100)
+    with open("random_data", "wb") as fout:
+        fout.write(random_data)
+
+    with open("random_data", "r+b") as fin:
+        mm = mmap.mmap(fin.fileno(), 0)
+        mm.seek(0)
+        mm.write(os.urandom(1024))
+        mm.flush()
+        mm.close()
+
+    print("done")
+
+
+if __name__ == "__main__":
+    main()


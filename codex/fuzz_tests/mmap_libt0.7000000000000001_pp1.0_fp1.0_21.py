import mmap
+import contextlib
+import os
+
+
+def main():
+    with open('random_file.txt', 'r') as f:
+        with contextlib.closing(mmap.mmap(f.fileno(), 0,
+                                          access=mmap.ACCESS_READ)) as m:
+            print m.readline()
+            print len(m)
+            print m.size()
+
+            with open('copy_file.txt', 'w') as f_copy:
+                f_copy.write(m)
+
+    # os.remove('random_file.txt')
+
+
+if __name__ == '__main__':
+    main()


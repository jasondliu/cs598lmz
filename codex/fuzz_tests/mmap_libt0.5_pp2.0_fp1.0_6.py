import mmap
+import time
+import sys
+import os
+
+#
+#
+#
+#
+#
+
+if len(sys.argv) < 2:
+    print "Usage: python %s [filename]" % sys.argv[0]
+    sys.exit()
+
+#
+#
+#
+#
+#
+
+def main():
+    while True:
+        try:
+            f = open(sys.argv[1], "r+")
+        except IOError:
+            time.sleep(1)
+            continue
+
+        break
+
+    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
+
+    while True:
+        s = m.readline()
+        if s == "":
+            time.sleep(1)
+            continue
+
+        if s == "quit\n":
+            break
+
+        print s
+
+    m.close()


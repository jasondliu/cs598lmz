import mmap
+import time
+
+f = open('testfile.txt', 'r')
+
+# Memory-map the file, size 0 means whole file
+mm = mmap.mmap(f.fileno(), 0)
+
+while True:
+    line = mm.readline()  # read one line
+    if not line:
+        print 'reached end of file'
+        break
+    print line
+    time.sleep(1)
+
+mm.close()


import mmap
+import sys
+import os
+
+def main(argv):
+    if len(argv) != 2:
+        print('Usage: %s <file>' % argv[0])
+        return 1
+    if not os.path.isfile(argv[1]):
+        print('"%s" is not a file' % argv[1])
+        return 1
+
+    # Open the file for reading
+    f = open(argv[1], "r+")
+    # Create the mmap wrapper
+    map = mmap.mmap(f.fileno(), 0)
+
+    # Read the whole file
+    print('File content: "%s"' % map[:])
+    # Read the first 20 bytes
+    print('First 20 bytes: "%s"' % map[:20])
+    # Read from byte 20 to byte 30
+    print('Bytes 20 to 30: "%s"' % map[20:30])
+    # Read from byte 10 to byte 20
+    print('Bytes 10 to 20

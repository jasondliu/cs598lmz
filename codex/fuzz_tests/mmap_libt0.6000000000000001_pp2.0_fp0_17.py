import mmap
+import os
+import struct
+import sys
+
+
+def main():
+    if len(sys.argv) != 3:
+        print 'Usage: %s <input.dat> <output.dat>' % sys.argv[0]
+        sys.exit(1)
+    in_filename = sys.argv[1]
+    out_filename = sys.argv[2]
+    in_size = os.path.getsize(in_filename)
+    with open(in_filename, 'rb') as in_file:
+        with open(out_filename, 'wb') as out_file:
+            in_map = mmap.mmap(in_file.fileno(), in_size, access=mmap.ACCESS_READ)
+            out_map = mmap.mmap(out_file.fileno(), in_size, access=mmap.ACCESS_WRITE)
+            # TODO: check file size
+            num_items = in_size / 8
+            for i in xrange(num

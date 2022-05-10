import mmap
+import os
+import sys
+
+def split(filehandler, delimiter, buf_size=4096):
+    buf = ""
+    done = False
+    while not done:
+        new_buf = filehandler.read(buf_size)
+        if not new_buf:
+            done = True
+            # raise StopIteration
+        else:
+            buf += new_buf
+            while(delimiter in buf):
+                pos = buf.index(delimiter)
+                yield buf[:pos]
+                buf = buf[pos + len(delimiter):]
+    if buf != "":
+        yield buf
+
+def get_file_dict(file_path):
+    f = open(file_path, 'r')
+    file_size = os.path.getsize(file_path)
+    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
+
+    file_dict = {}
+    for text in split(mm

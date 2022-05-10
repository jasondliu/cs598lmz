import mmap
+import os
+import re
+
+TIME_PATTERN = re.compile(r'^([0-9]{2}):([0-9]{2}):([0-9]{2}),([0-9]{3}) --> ([0-9]{2}):([0-9]{2}):([0-9]{2}),([0-9]{3})$')
+
+
+def txt_to_srt(filename):
+    with open(filename, 'rb') as file:
+        mm = mmap.mmap(file.fileno(), 0, prot=mmap.PROT_READ)
+
+        counter = 1
+        while True:
+            start_index = mm.find(b'\r\n\r\n')
+            if start_index == -1:
+                break
+            row_end_index = mm.find(b'\r\n\r\n', start_index + 1)
+            if row_end_index == -1:
+               

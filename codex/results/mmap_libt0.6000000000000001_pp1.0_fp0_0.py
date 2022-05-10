import mmap
+import re
+import subprocess
+from subprocess import Popen, PIPE
+import sys
+import tempfile
+import time
+
+
+def get_first_line(filename):
+    with open(filename, 'rb') as f:
+        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
+            if m.find(b'\n') != -1:
+                return m.readline()
+            return m.read()
+
+
+def get_last_line(filename):
+    with open(filename, 'rb') as f:
+        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
+            if m.rfind(b'\n') != -1:
+                m.seek(m.rfind(b'\n'))
+                return m.readline()
+            return m.read()
+
+
+def get_last_lines(filename, n

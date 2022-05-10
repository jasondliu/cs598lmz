import mmap
+import os
+import re
+import sys
+import time
+
+
+# global variables
+
+exit_flag = False
+
+
+# utility functions
+
+def exit(message):
+    global exit_flag
+    exit_flag = True
+    print(message)
+    sys.exit(0)
+
+def get_file_size(path):
+    return os.stat(path).st_size
+
+def get_file_contents(path):
+    with open(path, 'r') as file:
+        return file.read()
+
+def get_file_contents_mmap(path):
+    with open(path, 'r') as file:
+        return mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
+
+def get_file_contents_mmap_regex(path, pattern):
+    with open(path, 'r') as file:
+        memory_map = mmap.mmap(file.fil

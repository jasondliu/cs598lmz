import mmap
+
+
+# create a queue to communicate with the worker threads
+queueLock = threading.Lock()
+workQueue = queue.Queue(10)
+threads = []
+
+
+def is_func(line):
+    if re.match(r"^\s*[a-zA-Z_]+\s+[a-zA-Z_]+\s*\(.*\)", line):
+        return True
+    else:
+        return False
+
+
+def is_lib(line):
+    if re.match(r"^\s*\#include\s+<.*>", line):
+        return True
+    else:
+        return False
+
+
+def is_if(line):
+    if re.match(r"^\s*if\s*\(.*\)", line):
+        return True
+    else:
+        return False
+
+
+def is_for(line):
+    if re.match(r"^\s*for\s*\

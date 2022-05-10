import mmap
+
+
+def get_memory_usage(pid=None):
+    if pid is None:
+        pid = os.getpid()
+
+    with open('/proc/{}/statm'.format(pid), 'rb') as f:
+        statm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
+
+    return int(statm.readline().split()[0]) * 4096


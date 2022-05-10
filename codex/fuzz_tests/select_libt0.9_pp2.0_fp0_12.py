import select
+
+
+class SelectSocket:
+    def __init__(self, host, port, select_timeout=None):
+        self.host = host
+        self.port = port
+        self.select_timeout = select_timeout
+    
+    def __enter__(self):
+        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+        self.s.setblocking(False)
+        self.s.connect((self.host, self.port))
+        ready = select.select([], [self.s], [], self.select_timeout)
+        if ready[1]:
+            return self.s
+        else:
+            raise socket.error
+    
+    def __exit__(self, *_):
+        self.s.close()


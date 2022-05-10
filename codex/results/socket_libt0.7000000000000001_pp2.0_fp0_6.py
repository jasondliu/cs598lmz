import socket
+import time
+
+
+def get_local_ip():
+    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
+        s.connect(("8.8.8.8", 80))
+        return s.getsockname()[0]
+
+
+def get_local_timestamp():
+    return time.time()
+
+
+class Client:
+    def __init__(self, server_ip, server_port):
+        self.server_ip = server_ip
+        self.server_port = server_port
+        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+
+        self.local_ip = get_local_ip()
+        self.ts = get_local_timestamp()
+
+    def connect(self):
+        self.s.connect((self.server_ip, self.server_port))
+
+    def send(self, message):
+        self.s.

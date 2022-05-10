import socket
+import time
+import sys
+
+
+class Client:
+    def __init__(self, host, port, timeout=None):
+        self.host = host
+        self.port = port
+        self.timeout = timeout
+        self.sock = socket.create_connection((self.host, self.port), self.timeout)
+
+    def put(self, key, value, timestamp=None):
+        if not timestamp:
+            timestamp = int(time.time())
+        self.sock.sendall(f"put {key} {value} {timestamp}\n".encode("utf8"))
+        data = self.sock.recv(1024)
+        if data == b"ok\n\n":
+            return True
+        else:
+            raise ClientError
+
+    def get(self, key):
+        self.sock.sendall(f"get {key}\n".encode("utf8"))
+        data = self.sock.recv(1024)
+        if data

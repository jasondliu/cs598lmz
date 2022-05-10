import socket
+import time
+import sys
+
+
+class ClientError(Exception):
+    pass
+
+
+class Client:
+    def __init__(self, host, port, timeout=None):
+        self.host = host
+        self.port = port
+        self.timeout = timeout
+        try:
+            self.connection = socket.create_connection((self.host, self.port), self.timeout)
+        except socket.error as err:
+            raise ClientError("error create connection", err)
+
+    def put(self, key, value, timestamp=None):
+        timestamp = timestamp or int(time.time())
+        try:
+            self.connection.sendall(
+                f"put {key} {value} {timestamp}\n".encode("utf8")
+            )
+            data = self.connection.recv(1024).decode("utf8")
+            if data == 'ok\n\n':
+                return
+            raise ClientError
+        except socket.error as err:

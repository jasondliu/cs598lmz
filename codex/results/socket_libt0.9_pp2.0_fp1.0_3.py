import socket, time
+
+class ClientError(Exception):
+    pass
+
+class Client:
+    def __init__(self, host, port, timeout=None):
+        self.host = host
+        self.port = port
+        self.timeout = timeout
+
+    def put(self, key, value, timestamp=None):
+        timestamp = timestamp or int(time.time())
+
+        try:
+            with socket.create_connection((self.host, self.port), self.timeout) as s:
+                message = f'put {key} {value} {timestamp}\n'
+                s.sendall(message.encode())
+                data = s.recv(1024)
+                if data != b'ok\n\n':
+                    raise ClientError
+        except:
+            raise ClientError
+
+    def get(self, key):
+        result = {}
+        try:
+            with socket.create_connection((self.host, self.port), self.timeout) as s:
+               

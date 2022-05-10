import socket
+import time
+import re
+
+class Client:
+    def __init__(self, host, port, timeout=None):
+        self.host = host
+        self.port = port
+        self.timeout = timeout
+
+    def put(self, key, value, timestamp=None):
+        timestamp = timestamp or int(time.time())
+        with socket.create_connection((self.host, self.port), self.timeout) as sock:
+            sock.sendall("put {} {} {}\n".format(key, value, timestamp).encode('utf-8'))
+            data = sock.recv(1024)
+            return data.decode('utf-8')
+
+    def get(self, key):
+        with socket.create_connection((self.host, self.port), self.timeout) as sock:
+            sock.sendall("get {}\n".format(key).encode('utf-8'))
+            data = sock.recv(1024)
+            return data.decode('utf-8

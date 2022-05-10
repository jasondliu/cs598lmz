import socket
+
+
+class PythonHttpClient:
+    def __init__(self, hostname, port, ssl_connection=False, sock_timeout=0.1):
+        self.ip = None
+        self.resolve_hostname(hostname)
+        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+        self.sock.settimeout(sock_timeout)
+        self.sock.connect((self.ip, port))
+        if ssl_connection:
+            self.sock = ssl.wrap_socket(self.sock)
+        self.res = None
+
+    def __del__(self):
+        self.sock.close()
+
+    def resolve_hostname(self, hostname):
+        ips = socket.gethostbyname_ex(hostname)
+        self.ip = ips[2][0]
+        if not self.ip:
+            raise RuntimeError("can't resolve hostname: {0}".

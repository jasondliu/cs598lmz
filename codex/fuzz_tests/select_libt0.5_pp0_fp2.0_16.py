import select
+
+
+class Client:
+    def __init__(self, host, port):
+        self.host = host
+        self.port = port
+        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+        self.socket.connect((self.host, self.port))
+
+    def send(self, msg):
+        self.socket.send(msg)
+
+    def recv(self):
+        data = self.socket.recv(1024)
+        return data
+
+    def close(self):
+        self.socket.close()
+
+
+class Server:
+    def __init__(self, host, port):
+        self.host = host
+        self.port = port
+        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+        self.socket.bind((self.host, self.port))
+        self.socket.listen(5)
+
+    def accept

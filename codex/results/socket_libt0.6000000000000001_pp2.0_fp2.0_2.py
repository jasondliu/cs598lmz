import socket
+
+
+class Client:
+    def __init__(self, server, port):
+        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+        self.socket.connect((server, port))
+        self.stream = self.socket.makefile("rw")
+        self.name = None
+
+    def login(self, name):
+        self.socket.sendall(bytes(name, "utf8"))
+        response = self.stream.readline()
+        if response == "SUCCESS":
+            self.name = name
+        return response
+
+    def send(self, message):
+        self.socket.sendall(bytes(message, "utf8"))
+
+    def receive(self):
+        return self.stream.readline()
+
+    def close(self):
+        self.socket.close()
+
+
+class ClientThread(Thread):
+    def __init__(self, client):
+        super().__init__()

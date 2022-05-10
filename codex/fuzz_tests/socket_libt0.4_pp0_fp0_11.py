import socket
+import threading
+
+class Client:
+    def __init__(self, host, port):
+        self.host = host
+        self.port = port
+        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+        self.socket.connect((host, port))
+        self.socket.send(b"Hello, server")
+        self.run()
+
+    def run(self):
+        print("[*] Client started")
+        while True:
+            data = self.socket.recv(1024)
+            if not data:
+                break
+            print(data)
+
+if __name__ == "__main__":
+    client = Client("127.0.0.1", 9999)


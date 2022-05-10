import socket
+
+
+class Client:
+
+    def __init__(self, ip, port):
+        self.ip = ip
+        self.port = port
+        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+        self.sock.connect((ip, port))
+
+    def send(self, message):
+        self.sock.send(message.encode())
+        return self.sock.recv(1024)
+
+    def close(self):
+        self.sock.close()
+
+
+if __name__ == '__main__':
+    client = Client('localhost', 9090)
+    print(client.send('hello'))
+    client.close()


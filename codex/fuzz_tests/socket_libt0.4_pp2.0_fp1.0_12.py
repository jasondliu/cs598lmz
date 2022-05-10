import socket
+import sys
+import time
+
+
+class Client:
+    def __init__(self, ip, port):
+        self.ip = ip
+        self.port = port
+        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+        self.sock.connect((ip, port))
+
+    def send_message(self, message):
+        self.sock.send(message.encode())
+
+    def receive_message(self):
+        return self.sock.recv(1024).decode()
+
+
+def main():
+    client = Client(sys.argv[1], int(sys.argv[2]))
+    client.send_message("Hello")
+    print(client.receive_message())
+
+
+if __name__ == "__main__":
+    main()


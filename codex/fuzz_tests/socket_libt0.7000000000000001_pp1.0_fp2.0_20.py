import socket
+import sys
+import threading
+import time
+
+DEFAULT_SERVER_PORT = 12345
+DEFAULT_SERVER_HOST = 'localhost'
+
+DEFAULT_NUMBER_OF_CLIENTS = 10
+
+
+class Client:
+
+    def __init__(self, server_host, server_port, client_number):
+        self.server_host = server_host
+        self.server_port = server_port
+        self.client_number = client_number
+        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+        self.alive = True
+        self.connect()
+
+    def connect(self):
+        try:
+            self.sock.connect((self.server_host, self.server_port))
+        except ConnectionRefusedError:
+            print('Server is not available.')
+            sys.exit()
+        print('Connected to {}:{}'.format(self.server_host, self

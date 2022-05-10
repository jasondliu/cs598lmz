import socket
+
+class Client:
+    def __init__(self, host, port, mode):
+        self.host_ = host
+        self.port_ = port
+        self.mode_ = mode
+
+    def connect(self):
+        if self.mode_ == 'connect':
+            self.client_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+            self.client_.connect((self.host_, self.port_))
+        elif self.mode_ == 'listen':
+            self.client_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+            self.client_.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
+            self.client_.bind((self.host_, self.port_))
+            self.client_.listen(1)
+        else:
+            raise Exception("Wrong connection mode")
+
+    def send(self, cmd, message=''):
+

import select
+
+
+class TCPClient:
+    def __init__(self, host_ip, host_port):
+        self.host_ip = host_ip
+        self.host_port = host_port
+        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+        self.client_socket.connect((self.host_ip, self.host_port))
+        self.client_socket.setblocking(0)
+
+    def send(self, data):
+        self.client_socket.send(data)
+
+    def recv(self):
+        readable, _, _ = select.select([self.client_socket], [], [], 1)
+        if readable:
+            return self.client_socket.recv(1024)
+        else:
+            return None
+
+    @staticmethod
+    def send_request(data):
+        protocol = '{}\r\n\r\n'.format(data)
+        return protocol
+


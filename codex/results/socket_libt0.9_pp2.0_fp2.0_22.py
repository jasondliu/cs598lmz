import socket
+import sys
+
+
+class TCP_server():
+
+    def TCP_server(self, port):
+        self.server_ip = socket.gethostbyname(socket.gethostname())
+        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+        self.server_binding = (self.server_ip, port)
+        self.client_socket.bind(self.server_binding)
+        #self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
+        self.client_socket.listen(1)
+        print(self.server_ip)
+        while True:
+            self.conn, self.addr = self.client_socket.accept()
+            # server sends data to client
+            #self.data = "Hello Client!"
+            #self.conn.sendall(self.data.encode())
+            # server receives data from client
+            self.data = self.

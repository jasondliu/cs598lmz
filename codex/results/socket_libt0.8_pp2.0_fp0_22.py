import socket
+import sys
+
+
+class Server:
+    def __init__(self, host, port):
+        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
+        self.sock.bind((host, port))
+        self.sock.listen(5)
+        print('Server started on {0}:{1}'.format(host, port))
+
+    def listen(self):
+        try:
+            while 1:
+                connection, address = self.sock.accept()
+                data = connection.recv(4096)
+                print('Received request from {0}: {1}'.format(address, data))
+                connection.close()
+        except KeyboardInterrupt:
+            print('Closing connection')
+            self.sock.close()
+            sys.exit()
+
+
+if __name__

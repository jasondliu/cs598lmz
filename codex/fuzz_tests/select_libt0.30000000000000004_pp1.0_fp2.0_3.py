import select
+import socket
+import sys
+import time
+
+
+class Server:
+    def __init__(self, port=8080):
+        self.host = ''
+        self.port = port
+        self.open_socket()
+        self.clients = {}
+        self.size = 1024
+
+    def open_socket(self):
+        """ Setup the socket for incoming clients """
+        try:
+            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
+            self.server.bind((self.host, self.port))
+            self.server.listen(5)
+            self.server.setblocking(0)
+        except socket.error, (value, message):
+            if self.server:
+                self.server.close()
+            print "Could not open socket: " + message
+            sys.exit(1

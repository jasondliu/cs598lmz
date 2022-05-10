import socket
+from datetime import datetime
+import select
+
+
+class Server(object):
+    def __init__(self, port):
+        self.sock = socket.socket(socket.AF_INET,
+                                  socket.SOCK_STREAM)
+        self.sock.setsockopt(socket.SOL_SOCKET,
+                             socket.SO_REUSEADDR,
+                             1)
+        self.sock.bind(('localhost', port))
+        self.sock.listen(5)
+        self.clients = [self.sock]
+        self.buffer_size = 1024
+        self.end_string = "\r\n\r\n"
+
+    def run(self):
+        while True:
+            ready_to_read, ready_to_write, in_error = select.select(self.clients, [], [], 0)
+            for sock in ready_to_read:
+                if sock == self.sock:
+                    new_s

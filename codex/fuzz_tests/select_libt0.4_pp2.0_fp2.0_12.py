import select
+import socket
+import sys
+
+
+class Server:
+    def __init__(self, host, port):
+        self.host = host
+        self.port = port
+        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
+        self.server_socket.bind((self.host, self.port))
+        self.server_socket.listen(5)
+        self.inputs = [self.server_socket]
+        self.outputs = []
+        self.message_queues = {}
+
+    def run(self):
+        while True:
+            readable, writable, exceptional = select.select(
+                self.inputs, self.outputs, self.inputs)
+            for s in readable:
+                if s is self.server_socket:
+                    connection, client_address = s.

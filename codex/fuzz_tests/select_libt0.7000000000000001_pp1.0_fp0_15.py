import select
+import socket
+import sys
+import signal
+
+
+class Proxy:
+    def __init__(self):
+        self.host = "127.0.0.1"
+        self.port = int(sys.argv[1])
+        self.backlog = 5
+        self.size = 1024
+        self.server = None
+        self.threads = []
+
+    def open_socket(self):
+        try:
+            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+            self.server.bind((self.host, self.port))
+            self.server.listen(5)
+        except socket.error as e:
+            if self.server:
+                self.server.close()
+            print("Could not open socket: " + str(e))
+            sys.exit(1)
+
+    def run(self):
+        self.open_socket()
+        input = [self.server, sys.stdin]

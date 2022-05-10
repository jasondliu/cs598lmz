import select
+
+
+class Socket:
+    def __init__(self, host, port):
+        self.host = host
+        self.port = port
+        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+
+    def connect(self):
+        try:
+            self.socket.connect((self.host, self.port))
+        except Exception as e:
+            print("Error: " + str(e))
+            exit()
+
+    def send(self, data):
+        try:
+            self.socket.send(data.encode())
+        except Exception as e:
+            print("Error: " + str(e))
+            exit()
+
+    def recv(self):
+        try:
+            ready = select.select([self.socket], [], [], 2)
+            if ready[0]:
+                return self.socket.recv(4096)
+            else:
+                return False
+        except Exception as e:

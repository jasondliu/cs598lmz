import socket
+import sys
+import threading
+import time
+
+
+class Client:
+    def __init__(self, host, port, name):
+        self.host = host
+        self.port = port
+        self.name = name
+        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+        self.socket.connect((self.host, self.port))
+        self.socket.settimeout(2)
+
+        send_thread = threading.Thread(target=self.send_message)
+        send_thread.daemon = True
+        send_thread.start()
+
+        while True:
+            try:
+                data = self.socket.recv(1024)
+                if data:
+                    print(data.decode())
+            except:
+                time.sleep(0.1)
+
+    def send_message(self):
+        while True:
+            self.socket.sendall(self.name.encode() + b

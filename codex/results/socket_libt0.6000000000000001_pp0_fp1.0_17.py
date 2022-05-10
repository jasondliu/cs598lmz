import socket
+import threading
+
+#HOST = '127.0.0.1'
+HOST = '192.168.1.125'
+PORT = 65432
+
+def listen():
+    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
+        s.bind((HOST, PORT))
+        s.listen()
+        conn, addr = s.accept()
+        with conn:
+            print('Connected by', addr)
+            while True:
+                data = conn.recv(1024)
+                if not data:
+                    break
+                print(data.decode())
+                conn.sendall(data)
+
+def send():
+    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
+        s.connect((HOST, PORT))
+        while True:
+            s.sendall(b'Hello, world')
+            data = s.recv(1024)
+           

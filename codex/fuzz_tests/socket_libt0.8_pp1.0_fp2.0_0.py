import socket
+import time
+import datetime
+
+host = '127.0.0.1'
+port = 65432
+
+with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
+    s.bind((host, port))
+    s.listen()
+    conn, addr = s.accept()
+    with conn:
+        print('Connected by', addr)
+        while True:
+            data = conn.recv(1024)
+            now = datetime.datetime.now()
+            if not len(data):
+                break
+            conn.sendall(data)
+            print(data)


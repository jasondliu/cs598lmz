import socket
+
+
+def sock_server():
+    address = ('127.0.0.1', 30000)
+    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+    sk.bind(address)
+    sk.listen(5)
+
+    while True:
+        print("Waiting...")
+        conn, addr = sk.accept()
+        data = conn.recv(1024)
+        print('Data=' + data.decode('utf-8'))
+        conn.sendall(bytes('Hello', encoding='utf-8'))
+        conn.close()
+
+
+def sock_client():
+    address = ('127.0.0.1', 30000)
+    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+    sk.connect(address)
+    sk.sendall(bytes('Hello', encoding='utf-8'))
+    data = sk.recv(1024)
+    print('Data=' +

import socket
+from thread import start_new_thread
+
+#host = '127.0.0.1'
+host = '192.168.1.9'
+port = 9000
+s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+
+try:
+    s.bind((host, port))
+except socket.error as e:
+    print(str(e))
+
+s.listen(5)
+clients = []
+
+
+def threaded_client(conn):
+    conn.send('Welcome, type your info\n')
+
+    while True:
+        data = conn.recv(2048)
+        reply = 'Server output : ' + str(data)
+        if not data:
+            break
+        conn.sendall(reply)
+
+    conn.close()
+
+while True:
+    conn, addr = s.accept()
+    clients.append(conn)
+    print('Connected to :' + addr[0]

import socket
+import sys
+
+host = 'localhost'
+port = 8888
+
+s = None
+try:
+    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+    s.bind((host, port))
+    s.listen(1)
+    conn, addr = s.accept()
+    print 'Connected by', addr
+    while 1:
+        data = conn.recv(1024)
+        if not data: break
+        conn.send(data)
+except socket.error, msg:
+    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
+    sys.exit();
+
+conn.close()


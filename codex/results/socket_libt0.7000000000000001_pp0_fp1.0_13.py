import socket
+import sys
+
+HOST = ''
+PORT = 8888
+
+try:
+    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+except socket.error, msg:
+    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
+    sys.exit()
+
+print 'Socket Created'
+
+try:
+    socket.bind((HOST, PORT))
+except socket.error, msg:
+    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
+    sys.exit()
+
+print 'Socket bind complete'
+
+socket.listen(10)
+print 'Socket now listening'
+
+while 1:
+    conn, addr = socket.accept()
+    print 'Connected with ' + addr[0] + ':' + str(addr[1])
+    data = conn.recv(1024)
+

import socket
+
+
+
+def socket_create():
+    try:
+        global host
+        global port
+        global s
+        host = ''
+        port = 9999
+        s = socket.socket()
+    except socket.error as msg:
+        print("Socket creation error: " + str(msg))
+
+
+
+def socket_bind():
+    try:
+        global host
+        global port
+        global s
+        print("Binding socket to port: " + str(port))
+        s.bind((host, port))
+        s.listen(5)
+    except socket.error as msg:
+        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
+        socket_bind()
+
+
+def socket_accept():
+    conn, address = s.accept()
+    print("Connection has been established | " + "IP " + address[0] + " | Port " + str(address[1]))
+    send_commands

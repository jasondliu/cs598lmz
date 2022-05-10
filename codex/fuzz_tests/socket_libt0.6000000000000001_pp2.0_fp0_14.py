import socket
+
+host = socket.gethostname()
+port = 9999
+
+s = socket.socket()
+s.connect((host, port))
+
+message = input("-> ")
+while message != 'q':
+    s.send(message.encode('utf-8'))
+    data = s.recv(1024).decode('utf-8')
+    print("Received from server: " + data)
+    message = input("-> ")
+s.close()


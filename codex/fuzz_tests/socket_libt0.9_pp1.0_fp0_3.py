import socket
+
+host = '10.254.1.1'
+port = 65432
+
+s = socket.socket()
+s.connect((host, port))
+
+message = input('Enter Message : ')
+while message != 'bye' :
+    s.send(message.encode())
+    data = s.recv(1024).decode()
+    print('Message Received : ', data)
+    message = input('Enter Message : ')
+s.close()
+
+


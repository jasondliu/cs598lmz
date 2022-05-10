import socket
+
+s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+
+host = socket.gethostname()
+port = 12345
+
+s.connect((host, port))
+
+message = s.recv(1024)
+s.close()
+
+print(message.decode('ascii'))


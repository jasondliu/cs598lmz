import socket
+
+# create an socket object
+s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+
+# get local machine name
+host = socket.gethostname()
+
+port = 9999
+
+# connect to the server
+s.connect((host, port))
+
+# Receive no more than 1024 bytes
+msg = s.recv(1024)
+
+s.close()
+print(msg.decode('utf-8'))


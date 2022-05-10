import socket
+
+used_port = 65016
+serverSocket = socket(AF_INET,SOCK_STREAM)
+
+# Bind the socket to port used_port and wait for a connect request
+
+serverSocket.bind(('', used_port))
+serverSocket.listen(5)
+severSocket.settimeout(5.0)
+
+try:
+	c, addr = serverSocket.accept()
+	print 'client: ', addr
+	c.send('I am the server!')
+	c.close()
+except timeout:
+	print 'Connection timed out'
+serverSocket.close()


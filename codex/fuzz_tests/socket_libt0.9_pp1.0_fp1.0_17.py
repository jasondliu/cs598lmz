import socket
+client_socket = socket.socket()
+
+server_ip   = "localhost"
+server_port = 4444
+
+client_socket.connect((server_ip, server_port))
+
+
+while True:
+	command = raw_input("Command : ")
+	client_socket.send(command)
+	print "Output : "
+	print client_socket.recv(1024)
+
+client_socket.close()


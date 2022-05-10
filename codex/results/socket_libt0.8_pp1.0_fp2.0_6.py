import socket
+
+
+def main():
+	host = '10.10.9.66'
+	port = 1234
+
+	s = socket.socket()
+	s.connect((host,port))
+
+	message = input('-->')
+
+	s.send(message.encode())
+
+	data = s.recv(1024)
+
+	print('recieved from server: ' + data.decode())
+
+	s.close()
+
+if __name__ == '__main__':
+	main()


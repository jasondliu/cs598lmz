import socket
+import threading
+
+class EchoServer:
+	def __init__(self):
+		self.serverSocket = socket.socket()
+		self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
+		self.serverSocket.bind(('', 5000))
+		self.serverSocket.listen(5)
+
+	def start(self):
+		print('Server started!')
+		while True:
+			(clientSocket, client_address) = self.serverSocket.accept()
+			t = threading.Thread(target=self.client_handler, args=(clientSocket, client_address))
+			t.start()
+
+	def client_handler(self, clientSocket, client_address):
+		print('New client connected: {0}:{1}'.format(client_address[0], client_address[1]))
+		while True:
+			data = clientSocket.recv(

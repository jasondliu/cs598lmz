import socket
+
+BUFFER_SIZE = 4096
+
+class Client(threading.Thread):
+
+	def __init__(self,clientSocket,clientAddr):
+		threading.Thread.__init__(self)
+		self.clientSocket = clientSocket
+		self.clientAddr = clientAddr
+		self.clientName = None
+
+	def run(self):
+
+		msg = "Please enter your name: "
+		self.clientSocket.send(msg.encode())
+		self.clientName = self.clientSocket.recv(BUFFER_SIZE).decode()
+		print("\n" + self.clientName + " has joined the chat room")
+
+		while True:
+			try:
+				msg = self.clientSocket.recv(BUFFER_SIZE).decode()
+				
+				if msg == "":
+					raise Exception("Connection closed")
+
+			

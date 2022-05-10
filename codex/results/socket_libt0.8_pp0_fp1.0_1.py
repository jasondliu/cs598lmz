import socket
+import thread
+import time
+import struct
+
+def get_ip_address():
+	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
+	s.connect(("8.8.8.8", 80))
+	return s.getsockname()[0]
+
+def main():
+	ip = get_ip_address()
+	port = 8082
+
+	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
+	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
+	s.bind((ip, port))
+
+	print 'Server started!'
+	print 'Waiting for clients...'
+
+	while True:
+		data, addr = s.recvfrom(1024)
+		print 'Connected by', addr
+		if data == 'bye':
+			break
+		num = int(data)
+

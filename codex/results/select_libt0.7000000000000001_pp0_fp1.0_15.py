import select, os, sys, signal, re
+
+while True:
+	print('Waiting for connection ...')
+	try:
+		connection, client_address = sock.accept()
+	except IOError as e:
+		pass
+	else:
+		print('client connected:', client_address)
+		while True:
+			data = connection.recv(16)
+			print('received "%s"' % data)
+			if data:
+				print('sending data back to the client')
+				connection.sendall(data)
+			else:
+				print('no more data from', client_address)
+				break
+				
+				
+				
+				
+				
+				
+				
+				
+				
+				
+				
+				
+

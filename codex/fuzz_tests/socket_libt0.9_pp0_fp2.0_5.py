import socket   
+
+s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
+s.bind((host, port))
+s.listen(5)
+
+print "Server listening.."
+
+while True:
+
+	conn, addr = s.accept()
+	print "Connected by ",addr
+	
+	data = conn.recv(1024)
+	print "Server received : ",data
+	
+	filename = "mytext1.txt"
+	f = open(filename,'rb')
+	lenght =  os.path.getsize(filename)
+	l = f.read(lenght)
+	while(l):
+		conn.send(l)
+		print "Sent ",repr(l)
+		l = f.read(lenght)
+	f.close()
+	
+	print "Done sending"
+	
+	conn.send("Thank you for connecting")
+	conn.close()


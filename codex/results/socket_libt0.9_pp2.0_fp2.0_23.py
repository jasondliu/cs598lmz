import socket #import the socket module
+
+s = socket.socket() #Create a socket object
+host = socket.gethostname() #Get local machine name
+port = 12345 #Reserve a port for your service
+s.bind((host, port)) #Bind to the port
+
+s.listen(5) #Wait for the client connection
+while True:
+    c, addr = s.accept() #Establish a connection with the client
+    print 'Got connection from ', addr
+    c.send('Thank you for connecting')
+    c.close() #Close the connection


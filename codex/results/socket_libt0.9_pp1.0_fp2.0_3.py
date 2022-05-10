import socket
+import sys
+
+HOST = ''   # Symbolic name meaning all available interfaces
+PORT = 5001 # Arbitrary non-privileged port
+
+s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+print ('Socket created')
+
+#Bind socket to local host and port
+try:
+    s.bind((HOST, PORT))
+except socket.error as msg:
+    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
+    sys.exit()
+    
+print ('Socket bind complete')
+
+#Start listening on socket
+s.listen(10)
+print ('Socket now listening')
+
+#now keep talking with the client
+while 1:
+    #wait to accept a connection - blocking call
+    print('Esperando clientes...')
+    conn, addr = s.accept()
+    print('Cliente conectado')
+
+    #start new thread takes 1st argument as a function

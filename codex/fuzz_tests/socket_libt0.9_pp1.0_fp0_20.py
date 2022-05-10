import socket
+#to retrieve the date and time
+import datetime
+
+
+
+#to start the server
+s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
+host=''
+port=12345
+s.bind((host,port))
+s.listen(5)
+print('hello i am going to start the server now')
+
+#to connect to client
+while True:
+    clientsocket,addr=s.accept()
+    print('hello got a connection from ',addr)
+    dt = datetime.datetime.now()
+    Message = "current date and time:{}".format(dt)
+    #to send the date to client
+    clientsocket.send(Message.encode('ascii'))
+    clientsocket.close()
+
+
+
+
+


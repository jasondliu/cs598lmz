import select
+
+s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+s.bind((socket.gethostname(),1234))
+s.listen(5)
+
+while True:
+
+    #wait for connection
+    client_socket, address = s.accept()
+    print(f"Connection from {address} has been established")
+
+    client_socket.send(bytes("Welcome to the server!", "utf-8"))
+
+    while True:
+
+        msg = client_socket.recv(1024)
+        print(msg.decode("utf-8"))
+
+


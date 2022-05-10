import socket
+
+host=socket.gethostname()
+
+port=4444
+
+s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
+
+s.bind((host,port))
+
+
+print("Server started ",host)
+
+s.listen()
+
+conn,addr=s.accept()
+
+print("Connection from ",str(addr))
+
+while True:
+    msg=conn.recv(1024)
+    if not msg:
+        break
+    conn.send(msg.upper())
+
+conn.close()


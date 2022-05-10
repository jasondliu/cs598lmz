import socket
+
+host = "127.0.0.1"
+port = 8888
+
+s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+s.connect((host, port))
+
+while True:
+    message = input("Enter message to send: ")
+    message = message.encode()
+    s.sendall(message)
+    data = s.recv(1024)
+    print(data)
+s.close()


import socket
+
+host = ''
+port = 4040
+
+# creating the server socket object so that we can listen to the incoming request
+server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
+server_socket.bind((host, port))
+server_socket.listen(1)
+
+print("Waiting for connection . . . ")
+conn, address = server_socket.accept()  # accpeting any connection
+print("Connection from: " + str(address))
+
+while True:
+    data = conn.recv(1024).decode()  # receiving data from the client
+    if not data:
+        break
+
+    print("From connected user: " + str(data))
+    data = input(" -> ")
+    conn.send(data.encode())  # send data to client
+
+conn.close()  # close the connection

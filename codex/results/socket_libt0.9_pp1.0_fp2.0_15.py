import socket
+import sys
+
+# Create a TCP/IP socket
+sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+
+# Connect the socket to the port where the server is listening
+server_address = ("127.0.0.1", 10000)
+print("WARNING: EXECUTING ON " + server_address[0] + " Port: " + str(server_address[1]))
+print("keyfetch server started\n")
+
+sock.connect(server_address)
+
+while True: 
+    message = input("Enter your message: ")      
+    sock.sendall(message.encode())
+    data = sock.recv(3)
+    if data:
+        print(data)
+    else:
+        print("No Data")
+    continue
+
+sock.close()


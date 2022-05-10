import socket
+import sys
+import os
+
+def get_ip():
+  return socket.gethostbyname(socket.gethostname())
+
+def main():
+  # Create a TCP/IP socket
+  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+  # Bind the socket to the port
+  server_address = (get_ip(), 10000)
+  print('starting up on %s port %s' % server_address)
+  sock.bind(server_address)
+  # Listen for incoming connections
+  sock.listen(10)
+  while True:
+    # Wait for a connection
+    print('waiting for a connection')
+    connection, client_address = sock.accept()
+    print('connection from', client_address)
+    # Receive the data in small chunks and retransmit it
+    data = connection.recv(16)
+    print('received "%s"' % data)
+    if data:
+      print('sending data back to the client

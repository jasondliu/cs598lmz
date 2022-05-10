import socket
+import sys
+import threading
+
+# Create a TCP/IP socket
+sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+
+# Bind the socket to the port
+server_address = ('localhost', 10000)
+print >>sys.stderr, 'starting up on %s port %s' % server_address
+sock.bind(server_address)
+
+# Listen for incoming connections
+sock.listen(1)
+
+def handle_client(client_connection):
+    while True:
+        data = client_connection.recv(1024)
+        print >>sys.stderr, 'received "%s"' % data
+        if data:
+            client_connection.sendall(data)
+        else:
+            break
+    client_connection.close()
+
+while True:
+    # Wait for a connection
+    print >>sys.stderr, 'waiting for a connection'
+    connection, client_address = sock.accept()
+

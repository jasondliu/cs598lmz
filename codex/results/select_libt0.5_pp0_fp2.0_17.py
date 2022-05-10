import select
+import socket
+
+
+# create a socket
+# AF_INET: internet socket
+# SOCK_STREAM: TCP socket
+s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+
+# set socket options
+s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
+
+# bind socket to a port
+s.bind(('0.0.0.0', 12345))
+
+# start listening for incoming connections
+s.listen(5)
+
+# list of sockets
+sockets = [s]
+
+# list of clients
+clients = {}
+
+# list of client names
+names = {}
+
+# list of client name change requests
+name_requests = {}
+
+# list of client messages
+messages = {}
+
+
+def get_name(client):
+    # get name from client
+    name = client.recv(4096).decode

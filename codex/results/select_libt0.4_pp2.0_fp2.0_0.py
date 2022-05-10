import select
+
+
+def get_client_socket(host, port):
+    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+    client_socket.connect((host, port))
+
+    return client_socket
+
+
+def get_server_socket(host, port):
+    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+    server_socket.bind((host, port))
+    server_socket.listen(1)
+
+    return server_socket
+
+
+def get_client_socket_and_server_socket(host, port):
+    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+    client_socket.connect((host, port))
+
+    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+    server_socket.bind((host, port))
+    server_socket.listen(

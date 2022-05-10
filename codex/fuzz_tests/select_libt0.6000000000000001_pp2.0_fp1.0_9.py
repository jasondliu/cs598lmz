import select
+
+# create server socket
+server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+server_socket.bind(('localhost', 5000))
+server_socket.listen(5)
+
+# create epoll
+epoll = select.epoll()
+# register server socket for monitoring
+epoll.register(server_socket.fileno(), select.EPOLLIN)
+
+try:
+    connections = {}
+    requests = {}
+    responses = {}
+    while True:
+        events = epoll.poll(1)
+        for fileno, event in events:
+            if fileno == server_socket.fileno():
+                # accept connection
+                client_socket, address = server_socket.accept()
+                # register client socket for monitoring
+                epoll.register(client_socket.fileno(), select.EPOLLIN)
+                # store client socket
+                connections[client_socket.fileno()] = client_socket
+                requests[client_socket

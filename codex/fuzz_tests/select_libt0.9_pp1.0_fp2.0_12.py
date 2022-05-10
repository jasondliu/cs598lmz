import select
+
+server_address = "/tmp/server.sock"
+
+client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
+client_socket.connect(server_address)
+
+try:
+    message = client_socket.recv(4096)
+    print(message.decode())
+    if message:
+        text = input()
+        client_socket.sendall(text.encode(encoding="utf-8"))
+        # print(client_socket.recv(1024).decode())
+finally:
+    client_socket.close()
+
+


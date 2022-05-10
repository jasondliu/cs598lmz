import socket
+import json
+import threading
+
+def connection(sock):
+    try:
+        while True:
+            # Receive the data in small chunks and retransmit it
+            data = sock.recv(16)
+            print(data.decode('utf-8'))
+    except socket.error:
+        print('Close the connection')
+        sock.close()
+
+def port_open(port):
+    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+    result = sock.connect_ex(('127.0.0.1', port))
+    return result
+
+def list_clients(client_list):
+    print('List of connected clients:')
+    for client in client_list:
+        print(client)
+
+def send_cmd(sock, cmd):
+    try:
+        # Send data
+        message = cmd.encode('utf-8')
+        sock.sendall(message)
+    except socket

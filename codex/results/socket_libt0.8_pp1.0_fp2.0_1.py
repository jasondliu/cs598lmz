import socket
+
+client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+client.connect(('192.168.0.101', 8080))
+
+while True:
+    s = raw_input('input>')
+    client.sendall(s)
+    if s == 'quit':
+        break
+
+client.close()


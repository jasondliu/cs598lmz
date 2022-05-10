import socket
+
+
+s = socket.socket()
+s.connect(('localhost', 9999))
+
+while True:
+    print(s.recv(1024).decode('utf-8'))
+    data = input()
+    s.send(data.encode('utf-8'))
+    if data == 'exit':
+        break
+
+s.close()
+


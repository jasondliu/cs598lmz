import socket
+import threading
+import struct
+
+def send_cmd(socket, cmd):
+    print("Sending command: " + cmd)
+    socket.send(b'send <' + bytes(cmd, 'utf-8') + b'>')
+
+def recv_cmd(socket):
+    cmd = socket.recv(1024)
+    print("Received command: " + str(cmd, 'utf-8'))
+
+def send_str(socket, string):
+    print("Sending string: " + string)
+    socket.send(b'send <' + bytes(string, 'utf-8') + b'>')
+
+def recv_str(socket):
+    string = socket.recv(1024)
+    print("Received string: " + str(string, 'utf-8'))
+
+def send_int(socket, num):
+    print("Sending integer: " + str(num))
+    socket.send(b'send <' + bytes(str(num)) + b'>')


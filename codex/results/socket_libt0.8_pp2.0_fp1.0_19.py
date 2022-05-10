import socket
+import datetime
+import time
+import ssl
+import threading
+import os
+import random
+
+# AF_INET - a socket of family IPv4
+# SOCK_STREAM - a socket of type TCP
+serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
+serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
+serverSocket.connect(('127.0.0.1', 10345))
+
+#serverSocket = ssl.wrap_socket(serverSocket)
+
+serverSocket.sendall(b'Hello, server!')
+data = serverSocket.recv(1024)
+print('received', repr(data))
+serverSocket.close()


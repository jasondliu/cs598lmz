import socket
+import time
+import sys
+from _thread import *
+HOST = 'localhost'
+PORT = int(sys.argv[1])
+BUFSIZ = 1024
+ADDR = (HOST, PORT)
+
+tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+tcpSerSock.bind(ADDR)
+tcpSerSock.listen(5)
+
+def clientthread(conn, addr, item_stock, item_stock_lock, log, log_lock):
+    BUFSIZ = 1024
+    while True:
+        data = conn.recv(BUFSIZ)
+        if not data:
+            break
+        else:
+            data = data.decode()
+            if data == 'exit':
+                break
+            else:
+		tokens = data.split(',')
+		if tokens[0] == 'SetStock':
+		    item_stock_lock.acquire()
+	

import socket
+import time
+
+
+def recv(sk):
+    with sk:
+        while True:
+            data = sk.recv(1024)
+            if not data:
+                exit()
+            print(data)
+
+
+def send(sk):
+    with sk:
+        while True:
+            msg = input(">> ")
+            sk.sendall(bytes(msg, 'utf-8'))
+
+
+def client():
+    host = socket.gethostname()
+    port = 9999
+
+    sk = socket.socket()
+    sk.connect((host, port))
+
+    t_recv = threading.Thread(target=recv, args=(sk,))
+    t_send = threading.Thread(target=send, args=(sk,))
+    t_recv.start()
+    t_send.start()
+    # t_recv.join()
+    # t_send.join()
+
+
+def server():


import socket, threading, time
+
+
+# 创建多线程类
+class ThreadedServer(object):
+    def __init__(self, host, port):
+        self.host = host
+        self.port = port
+        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
+        self.sock.bind((self.host, self.port))
+
+    # 创建线程
+    def listen(self):
+        self.sock.listen(5)
+        while True:
+            client, address = self.sock.accept()
+            client.settimeout(60)
+            threading.Thread(target=self.listenToClient, args=(client, address)).start()
+
+    # 接受Client端请

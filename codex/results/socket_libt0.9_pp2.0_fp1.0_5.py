import socket
+import time
+import threading
+
+s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+
+firstpoint = ("127.0.0.1",31311)
+firstpoint_to = ("127.0.0.1",31312)
+
+s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
+s.connect(firstpoint_to)
+print("connect to server :", firstpoint_to)
+
+def sendmsg():
+    while True:
+        str = input("please input :")
+        s.send(str.encode("utf-8"))
+        if str == "exit":
+            s.send(str.encode("utf-8"))
+            break
+
+def recvmsg():
+    while True:
+        data = s.recv(1024)
+        if data:
+            print("\n从：",firstpoint_to, " 收到

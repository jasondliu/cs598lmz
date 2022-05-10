import socket
+import json
+import threading
+
+
+# 定义全局变量
+HOST = '0.0.0.0'
+PORT = 8888
+
+
+# 构建套接字
+s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+
+# 绑定IP和端口
+s.bind((HOST, PORT))
+
+# 设置监听
+s.listen(5)
+
+# 全局字典，保存所有连接的客户端
+all_connections = {}
+all_addresses = {}
+
+
+# 接收连接请求
+def accept_connections():
+    while True:
+        conn, addr = s.accept()
+        #

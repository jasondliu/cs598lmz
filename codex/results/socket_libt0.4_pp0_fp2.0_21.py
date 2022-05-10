import socket
+import time
+import threading
+import sys
+
+
+def get_host_ip():
+    """
+    获取本机ip地址
+    :return: ip
+    """
+    try:
+        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
+        s.connect(('8.8.8.8', 80))
+        ip = s.getsockname()[0]
+    finally:
+        s.close()
+
+    return ip
+
+
+def get_time():
+    """
+    获取当前时间
+    :return:
+    """
+    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
+
+
+def tcp_server(port):
+    """
+    创建tcp服务器
+    :param port:

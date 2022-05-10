import socket
+
+
+def get_local_ip():
+    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
+    s.connect(('8.8.8.8', 80))
+    ip = s.getsockname()[0]
+    s.close()
+    return ip
+
+
+def get_remote_ip(url):
+    try:
+        ip = socket.gethostbyname(url)
+        return ip
+    except Exception:
+        return None
+
+
+def get_local_ip_info(ip):
+    try:
+        info = socket.gethostbyaddr(ip)
+        return info
+    except Exception:
+        return None
+
+
+def get_remote_ip_info(ip):
+    try:
+        info = socket.gethostbyaddr(ip)
+        return info
+    except Exception:
+        return None
+
+
+def get_local_ip_info_by_asyn

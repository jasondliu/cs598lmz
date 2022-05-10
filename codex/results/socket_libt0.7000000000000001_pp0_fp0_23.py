import socket
+
+
+def getLocalIP():
+    """
+    获取本地ip地址
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
+def getOutIP(url):
+    """
+    获取外网ip地址
+    :param url: "http://2018.ip138.com/ic.asp"
+    :return: ip
+    """
+    try:
+        req = urllib.request.urlopen(url)
+        req.encoding = 'gbk'
+        result = req.read().decode('gbk')
+        # print(result)
+        ip = re

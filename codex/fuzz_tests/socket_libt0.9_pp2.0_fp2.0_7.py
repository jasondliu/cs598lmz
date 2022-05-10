import socket
+
+def get_ip_address():
+    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
+    s.connect(('8.8.8.8', 1)) #Google DNS server
+    return s.getsockname()[0]
+
+
+print get_ip_address()
+
+## or use this, too slow:
+# import urllib
+# print urllib.urlopen('http://ip.42.pl/raw').read()


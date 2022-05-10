import socket
+from urllib.parse import urlparse
+from selectors import DefaultSelector, EVENT_READ
+from pymysql import connect
+
+selector = DefaultSelector()
+urls_todo = set(['/'])
+seen_urls = set(['/'])
+stopped = False
+conns = set()
+conns_wt = set()
+#Mysql连接配置
+conn = connect(host='localhost', port=3306, user='root', password='123456', db='spider', charset='utf8')
+cursor = conn.cursor()
+
+
+class Fetcher:
+    def __init__(self, url):
+        self.response = b''  # Buffer
+        self.url = url
+        self.sock = None
+
+    def fetch(self):
+        self.sock = socket.socket()
+        self.sock.setblocking(False)
+        #断点1
+        #

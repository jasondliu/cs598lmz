import socket
+#socket.setdefaulttimeout(900)
+import CONST
+
+class Server(object):
+	"""docstring for Server"""
+	def __init__(self, ip_addr=CONST.LOCAL_IP, port=CONST.LOCAL_PORT, addr=("", CONST.LOCAL_PORT)):
+		super(Server, self).__init__()
+		self._ip_addr = ip_addr
+		self._port = port
+		self._addr = addr
+	
+	def _start(self):
+		print "Server Start"
+
+	def _listen(self):
+		print "Server Listen"
+	
+	def _send_to(self, addr=("", CONST.LOCAL_PORT), msg=""):
+		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
+		s.sendto(msg, addr)
+		s.close()
+	
+
+
+
+	def

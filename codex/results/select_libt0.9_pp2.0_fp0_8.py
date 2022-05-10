import select
+
+
+class Client(threading.Thread):
+	def __init__(self, conn, addr, port):
+		threading.Thread.__init__(self)
+		self.conn = conn
+		self.addr = addr
+		self.port = port
+		self.running = False
+		self.data = [[]] * 5 # NOTE: Contains [[x, y], [px, py], [rx, ry], [vx, vy], [flexs]]
+		self.sensitivity = 0.4 # The amount of acceleration allowed
+
+	def run(self):
+		self.running = True
+		print("Started client thread. Listening on port", self.port)
+		while self.running:
+			try:
+				r, w, x = select.select([self.conn], [self.conn], [])
+				if self.conn in r:
+					buf = self.conn.recv(1024)

import select
+
+
+class Client:
+    def __init__(self, host, port, username, password):
+        self.host = host
+        self.port = port
+        self.username = username
+        self.password = password
+
+    def connect(self):
+        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+        self.sock.connect((self.host, self.port))
+        self.sock.sendall('{}\n{}\n'.format(self.username, self.password))
+
+    def get_input(self):
+        r, _, _ = select.select([sys.stdin], [], [])
+        if r:
+            return sys.stdin.readline()
+        else:
+            return None
+
+    def run(self):
+        self.connect()
+        while True:
+            data = self.sock.recv(1024)
+            if not data:
+                break
+

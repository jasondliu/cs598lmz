import socket
+
+class MysqlClient:
+
+  def __init__(self):
+    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+    self.s.connect(('127.0.0.1', 5555))
+
+  def __del__(self):
+    self.s.close()
+
+  def query(self, query):
+    self.s.send(query)
+    resp = ''
+    buff = ''
+    while True:
+      buff = self.s.recv(1024)
+      if not buff: break
+      resp += buff
+    return resp
+
+
+if __name__ == '__main__':
+  client = MysqlClient()
+  while True:
+    query = raw_input(">> ")
+    print client.query(query)


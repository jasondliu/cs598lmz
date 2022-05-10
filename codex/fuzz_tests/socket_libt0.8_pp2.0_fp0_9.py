import socket
+
+
+class Server:
+    s = socket.socket()
+    host = socket.gethostname()
+    port = 12345
+
+
+    def __init__(self):
+        pass
+
+    def read(self):
+        print("Hello")
+        self.s.connect((self.host, self.port))
+        print(self.s.recv(1024))
+        self.s.close()
+        pass
+
+    def write(self):
+        self.s.bind((self.host, self.port))
+        self.s.listen(5)
+
+        while True:
+            c, addr = self.s.accept()
+            print('Got connection from', addr)
+            c.send(b'Thank you for connecting')
+            c.close()
+
+
+if __name__ == '__main__':
+    app = Server()
+    app.read()
+    #app.write()


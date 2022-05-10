import socket
+import threading
+
+
+class Tcp_Server:
+    def __init__(self):
+        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+        self.sock.bind(("127.0.0.1", 8000))
+        self.sock.listen(10)
+
+    def listen(self):
+        while True:
+            conn, addr = self.sock.accept()
+            print("连接地址：%s" % str(addr))
+            t = threading.Thread(target=self.work, args=(conn, addr))
+            t.start()
+
+    def work(self, conn, addr):
+        while True:
+            data = conn.recv(1024)
+            print("接受到的数据：", data)
+            conn.send(data)
+
+
+if __name__ == '__main__':


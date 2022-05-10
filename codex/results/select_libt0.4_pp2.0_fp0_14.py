import select
+
+
+def main():
+    server = socket.socket()
+    server.bind(('0.0.0.0', 8000))
+    server.listen()
+
+    conn1, addr1 = server.accept()
+    conn2, addr2 = server.accept()
+
+    epoll = select.epoll()
+    epoll.register(conn1.fileno(), select.EPOLLIN | select.EPOLLET)
+    epoll.register(conn2.fileno(), select.EPOLLIN | select.EPOLLET)
+
+    conn_dict = {
+        conn1.fileno(): conn1,
+        conn2.fileno(): conn2
+    }
+
+    while True:
+        events = epoll.poll()
+        for fileno, event in events:
+            if event & select.EPOLLIN:
+                recv_data = conn_dict[fileno].recv(1024)
+                print(recv_data.decode('utf8'))

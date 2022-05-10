import socket
+from threading import Thread
+
+
+def main():
+    host = '127.0.0.1'
+    port = 5555
+
+    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+    s.bind((host, port))
+    s.listen()
+
+    while True:
+        conn, addr = s.accept()
+        print('Connected to:', addr)
+        Thread(target=server, args=(conn, addr)).start()
+
+
+def server(conn, addr):
+    while True:
+        data = conn.recv(2048)
+        if not data:
+            break
+        print('Received from:', addr, '\nData:', data.decode())
+        conn.send(data.upper())
+    conn.close()
+
+
+if __name__ == '__main__':
+    main()


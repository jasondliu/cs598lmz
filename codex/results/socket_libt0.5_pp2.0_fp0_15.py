import socket
+
+
+def main():
+    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+    s.bind(('127.0.0.1', 1234))
+    s.listen(1)
+    while True:
+        conn, addr = s.accept()
+        while True:
+            data = conn.recv(1024)
+            if not data:
+                break
+            conn.send(data)
+        conn.close()
+
+
+if __name__ == '__main__':
+    main()


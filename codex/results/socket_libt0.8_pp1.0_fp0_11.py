import socket
+import sys
+
+PORT = 8990
+
+
+def main():
+    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
+    s.bind(('', PORT))
+    s.listen(1)
+    print "Listening on port %s" % PORT
+    while 1:
+        conn, addr = s.accept()
+        data = conn.recv(1024)
+        while 1:
+            if not data:
+                break
+            conn.sendall(data)
+            data = conn.recv(1024)
+        print "Connection closed"
+        conn.close()
+
+if __name__ == '__main__':
+    main()


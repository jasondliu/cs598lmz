import socket
+import sys
+
+if len(sys.argv) != 3: 
+    print("Usage: $0 IP PORT")
+    exit(1)
+
+s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+
+s.connect((sys.argv[1], int(sys.argv[2])))
+
+while True:
+    data = s.recv(1024)
+    if not data:
+        break
+    sys.stdout.write(data.decode("utf-8"))
+
+s.close()


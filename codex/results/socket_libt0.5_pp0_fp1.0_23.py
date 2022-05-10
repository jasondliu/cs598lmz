import socket
+import threading
+import os
+import time
+
+
+def connect(ip, port, file):
+    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+    s.connect((ip, port))
+    s.send(file)
+    s.close()
+
+
+def main():
+    if len(sys.argv) != 4:
+        print("Usage: " + sys.argv[0] + " <IP> <port> <file>")
+        sys.exit(0)
+
+    ip = sys.argv[1]
+    port = int(sys.argv[2])
+    file_name = sys.argv[3]
+
+    if not os.path.isfile(file_name):
+        print("[-] " + file_name + " does not exist.")
+        sys.exit(0)
+
+    if not os.access(file_name, os.R_OK):
+        print("[-

import socket
+import time
+import sys
+
+
+
+def main():
+    if len(sys.argv) < 2:
+        print("Please enter a file name")
+        sys.exit()
+    else:
+        filename = sys.argv[1]
+    host = '127.0.0.1'
+    port = 5000
+
+
+
+    s = socket.socket()
+    s.connect((host,port))
+    s.send(filename.encode())
+    data = s.recv(1024)
+    if data[:6] == 'EXISTS':
+        filesize = int(data[6:])
+        message = input("File exists, " + str(filesize) +"Bytes, download? (Y/N)? -> ")
+        if message == 'Y':
+            s.send('OK'.encode())
+            f = open('new_'+filename, 'wb')
+            data = s.recv(1024)
+            totalRecv = len(

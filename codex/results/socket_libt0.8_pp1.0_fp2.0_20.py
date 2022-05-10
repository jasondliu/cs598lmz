import socket
+
+def recvall(sock):
+    BUFF_SIZE = 4096 # 4 KiB
+    data = b''
+    while True:
+        part = sock.recv(BUFF_SIZE)
+        data += part
+        if len(part) < BUFF_SIZE:
+            # either 0 or end of data
+            break
+    return data
+
+s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+s.bind(('127.0.0.1', 1234))
+s.listen(1)
+conn, addr = s.accept()
+print("Connection from", addr)
+while True:
+    data = conn.recv(1024)
+    if (data):
+        #if(data=='image'):
+        print("received image")
+        stringData = recvall(conn)
+        #data = conn.recv(1024)
+        #print("received image")
+        with open('image.jpg','wb') as image

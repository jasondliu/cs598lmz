import socket
+
+
+def send_file(sock, request):
+    requested_file = request[2:].strip()
+    if os.path.isfile(requested_file):
+        data = b''
+        with open(requested_file, 'br') as r_file:
+            for line in r_file.readlines():
+                data += line
+
+        data += b'\r\n\r\n'
+        print("data sent to client")
+        sock.sendall(data)
+    else:
+        print("not a file")
+        sock.sendall(b'not a file')
+
+
+def process_client(sock, client_addr):
+    print("Accepting connection from ", client_addr)
+
+    while True:
+        request = sock.recv(1024).decode()
+        print("Request received: ", request)
+
+        if request[:4] == 'FILE':
+            send_file(sock, request)
+
+       

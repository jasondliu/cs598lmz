import selectors
+import socket
+
+
+HOST = '127.0.0.1'  
+PORT = 65432
+
+messages = [b'Message 1 from client.', b'Message 2 from client.']
+
+sel = selectors.DefaultSelector()
+lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+lsock.bind((HOST, PORT))  
+lsock.listen()
+lsock.setblocking(False)  
+sel.register(lsock, selectors.EVENT_READ, data=None)
+
+
+def accept_wrapper(sock):
+    conn, addr = sock.accept()  # Should be ready to read
+    print('accepted connection from', addr)
+    conn.setblocking(False)
+    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
+    events = selectors.EVENT_READ | selectors.EVENT_WRITE
+    sel.register

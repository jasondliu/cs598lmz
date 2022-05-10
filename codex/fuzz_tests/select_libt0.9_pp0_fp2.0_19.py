import selectors
+import socket
+
+host = '127.0.0.1'  # Standard loopback interface address (localhost)
+port = 65432        # Port to listen on (non-privileged ports are > 1023)
+
+sel = selectors.DefaultSelector()
+keep_running = True
+
+
+lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+lsock.bind((host, port))
+lsock.listen()
+print('listening on', (host, port))
+lsock.setblocking(False)
+sel.register(lsock, selectors.EVENT_READ, data=None)
+
+while keep_running:
+    events = sel.select()
+    for key, mask in events:
+        if key.data is None:
+            accept_wrapper(key.fileobj)
+        else:
+            service_connection(key, mask)


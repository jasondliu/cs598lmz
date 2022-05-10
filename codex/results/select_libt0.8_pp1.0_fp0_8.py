import selectors
+import traceback
+from time import sleep
+from random import choice
+
+
+TIMEOUT = .001
+
+servers = [
+    ('www.google.com', 80),
+    ('www.facebook.com', 80),
+    ('www.twitter.com', 80),
+    ('www.instagram.com', 80),
+]
+
+
+def handle_connection(key, mask):
+    sock = key.fileobj
+    data = key.data
+    if mask & selectors.EVENT_READ:
+        recv_data = sock.recv(1024)
+        if recv_data:
+            data.response = recv_data
+        else:
+            print('Closed socket ', sock.getpeername())
+            sel.unregister(sock)
+            sock.close()
+    if mask & selectors.EVENT_WRITE:
+        request = data.request
+        if request:
+            data.request = None
+            sock.send(request)

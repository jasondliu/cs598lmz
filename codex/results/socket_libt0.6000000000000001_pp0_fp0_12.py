import socket
+import sys
+
+s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+
+server_address = ('localhost', 10000)
+print >>sys.stderr, 'connecting to %s port %s' % server_address
+s.connect(server_address)
+
+try:
+    
+    message = 'This is the message.  It will be repeated.'
+    print >>sys.stderr, 'sending "%s"' % message
+    s.sendall(message)
+
+    amount_received = 0
+    amount_expected = len(message)
+    
+    while amount_received < amount_expected:
+        data = s.recv(16)
+        amount_received += len(data)
+        print >>sys.stderr, 'received "%s"' % data
+
+finally:
+    print >>sys.stderr, 'closing socket'
+    s.close()


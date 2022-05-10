import socket
+import sys
+
+
+class MultiClientServer:
+
+    def __init__(self, port):
+        # Create a TCP/IP socket
+        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+
+        # Connect the socket to the port where the server is listening
+        server_address = ('localhost', port)
+        print 'connecting to %s port %s' % server_address
+        self.sock.connect(server_address)
+
+    def joining(self):
+        try:
+            # Send id
+            self.sock.sendall(self.id)
+
+            # Wait for welcome
+            amount_received = 0
+            amount_expected = len(self.id)
+
+            if amount_received < amount_expected:
+                data = self.sock.recv(1024)
+                amount_received += len(data)
+
+            print 'received "%s"' % data
+        except:
+            print

import select
+import socket
+import struct
+import sys
+import threading
+import time
+
+# We can run this on any available port since you can only
+# have one program listening to a port at a time
+MYPORT = 50008
+# The size of the UDP datagrams we send and receive
+BUFSIZE = 2048
+
+def usage():
+    sys.stderr.write('usage: echo-udpcliserver.py server [server2 ...]\n')
+    sys.exit(2)
+
+class ServerHandler(threading.Thread):
+    def __init__(self, client, address):
+        threading.Thread.__init__(self)
+        self.client = client
+        self.address = address
+
+    def run(self):
+        data = self.client.recv(BUFSIZE)
+        # Look for the b'\0' ending in the data
+        end = data.find(b'\0')
+        if end >= 0:
+            sys.stdout

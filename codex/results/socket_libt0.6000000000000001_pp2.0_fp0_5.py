import socket
+import os
+from threading import Thread
+from SocketServer import ThreadingMixIn
+
+TCP_IP = 'localhost'
+TCP_PORT = 9001
+BUFFER_SIZE = 1024
+
+class ClientThread(Thread):
+
+    def __init__(self,ip,port,sock):
+        Thread.__init__(self)
+        self.ip = ip
+        self.port = port
+        self.sock = sock
+        print " New thread started for "+ip+":"+str(port)
+
+    def run(self):
+        filename='mytext.txt'
+        f = open(filename,'rb')
+        while True:
+            l = f.read(BUFFER_SIZE)
+            while (l):
+                self.sock.send(l)
+                #print('Sent ',repr(l))
+                l = f.read(BUFFER_SIZE)
+            if not l:
+                f.close()
+                self.sock.close()


import weakref
+
+class Logger(object):
+    def __init__(self, file):
+        self.file = open(file, 'a')
+    
+    def log(self, msg):
+        self.file.write(msg + "\n")
+        print msg#
+
+    def __del__(self):
+        self.file.close()
+
+class Collector(object):
+    def __init__(self):
+        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
+        self.sock.bind(('', 5678))
+
+    def start(self):
+        self._loop = True
+        self._collect()
+    
+    def stop(self):
+        self._loop = False
+
+    def _collect(self):
+        while self._loop:
+            data = self.sock.recv(1024)
+            print "data: ", data
+
+class FrontendServer(object):
+    def __

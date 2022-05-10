import socket
+
+
+class opal:
+    def __init__(self, url, port, timeout=5, expose_request=False, expose_response=False):
+        self.url = url
+        self.port = port
+        self.timeout = timeout
+        self.expose_request = expose_request
+        self.expose_response = expose_response
+
+    def _send(self, request, timeout=None):
+        if not timeout:
+            timeout = self.timeout
+
+
+        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
+        s.settimeout(timeout)
+        try:
+            s.connect((self.url, self.port))
+        except socket.timeout:
+            if self.expose_request:
+                print "request:" + "\r\n" + request
+            if self.expose_response:
+                print "timeout"
+            return None
+        except:
+            if self.expose_request:
+

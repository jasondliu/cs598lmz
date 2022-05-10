import select
+
+from time import time
+from threading import Thread
+from tempfile import mkdtemp
+from sys import stdin
+
+
+class ThreadedServer(Thread):
+    """Threaded Server to handle requests from the client."""
+    def __init__(self, host, port):
+        """Initialize the ThreadedServer class"""
+        self.host = host
+        self.port = port
+        self.tempdir = mkdtemp()
+        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
+        self.sock.bind((self.host, self.port))
+
+        self.poller = select.poll()
+        self.poller.register(self.sock.fileno(), select.POLLIN)
+        self.poller.register(stdin.fileno(), select.POLLIN)
+
+       

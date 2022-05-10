import select
+import logging
+import traceback
+import sys
+
+class Client:
+    def __init__(self, host: str, port: int):
+        # logging
+        self.logger = logging.getLogger(__file__)
+        self.logger.setLevel(logging.DEBUG)
+        # console handler
+        console = logging.StreamHandler()
+        console.setLevel(logging.DEBUG)
+        console.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
+        self.logger.addHandler(console)
+
+        # socket setup
+        self.socket = None
+        self.host = host
+        self.port = port
+
+    def connect(self):
+        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+        self.logger.info("Connecting to host: %s, port: %d", self.

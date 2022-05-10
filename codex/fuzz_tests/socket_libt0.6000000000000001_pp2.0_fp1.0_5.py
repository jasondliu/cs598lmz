import socket
+import threading
+import json
+import logging
+
+
+class ChatClient:
+    def __init__(self, host, port):
+        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+        self.sock.connect((host, port))
+        self.sock.setblocking(0)
+        self.sock.settimeout(1)
+
+        self.logger = logging.getLogger('chat_client')
+
+        self.__msg_handler = {
+            'message': self.logger.info
+        }
+
+        self.__stop_event = threading.Event()
+        self.__thread = threading.Thread(target=self.__receive)
+        self.__thread.start()
+
+    def __receive(self):
+        while not self.__stop_event.is_set():
+            try:
+                data = self.sock.recv(1024)
+            except socket.

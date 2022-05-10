import select
+
+
+class Client:
+    def __init__(self, host, port, timeout=None):
+        self.host = host
+        self.port = port
+        self.timeout = timeout
+
+        try:
+            self.sock = socket.create_connection((host, port), timeout)
+        except socket.error as err:
+            raise ClientError("Error connection to server", err)
+
+    def _read(self):
+        """
+        Read message from server
+        :return: string
+        """
+        data = b""
+
+        # We are reading until we got \n symbol
+        while not data.endswith(b"\n\n"):
+            try:
+                data += self.sock.recv(1024)
+            except socket.error as err:
+                raise ClientError("Error recv data", err)
+
+        # Decode data from utf-8 to string
+        decoded_data = data.decode()
+
+        status

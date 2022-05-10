import socket, select
+from auth_logger import AuthLogger
+
+# Configure the logger
+AuthLogger.configure_logger()
+
+# Setup logger
+logger = AuthLogger.logger
+
+class Server:
+    def __init__(self):
+        """
+        Initializer for the server class
+        """
+        self.peers = [] # array of peers
+
+    def initiate_socket(self):
+        """
+        Initiate the socket for TCP communication
+        """ 
+        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
+
+    def bind_socket(self, host, port):
+        """
+        Bind the socket
+        """
+        self.server_socket.bind((host, port))
+
+    def listen_for_client(self):
+        self.

import select
+
+sys.path.append(os.path.realpath(os.path.abspath(__file__)) + '/../../../')
+from script.util.Printer import Printer
+
+# use "sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)" to reuse address
+
+
+class IpServer:
+    """
+    Class for IP server
+    """
+
+    def __init__(self, address='', port=8888, buf_size=4096):
+        assert type(address) is str, "param 'address' must be str"
+        assert type(port) is int, "param 'port' must be int"
+
+        self.address = address
+        self.port = port
+        self.buf_size = 4096
+
+        self.listen_socket = socket.socket()
+        self.listen_socket.bind((address, port))
+        self.listen_socket.listen(1)
+        print('Listen on

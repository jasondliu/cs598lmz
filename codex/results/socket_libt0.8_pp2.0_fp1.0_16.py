import socket
+import os
+import sys
+
+
+#AF_INET(ipv4)、AF_INET6(ipv6)、AF_UNIX(UNIX域)
+#socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+#socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
+#socket.socket(socket.AF_INET, socket.SOCK_RAW)
+
+#对于TCP协议来说，socket对象可以通过以下操作获得有关TCP连接的信息：
+#   socket.getsockname()返回socket连接发起方的地址。
+#   socket.getpeername()返回socket连接接收方的地址。
+#   socket

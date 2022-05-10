import socket
+import subprocess
+import sys
+from datetime import datetime
+
+subprocess.call('clear', shell=True)
+
+def is_valid_ipv4_address(address):
+    try:
+        socket.inet_pton(socket.AF_INET, address)
+    except AttributeError:
+        try:
+            socket.inet_aton(address)
+        except (socket.error, TypeError):
+            return False
+        return address.count('.') == 3
+    except socket.error:
+        return False
+    return True
+
+def is_valid_ipv6_address(address):
+    try:
+        socket.inet_pton(socket.AF_INET6, address)
+    except socket.error:
+        return False
+    return True
+
+if is_valid_ipv4_address(sys.argv[1]):
+    remote_server = socket.gethostbyname(sys.argv[1])
+    remote_server_ipv

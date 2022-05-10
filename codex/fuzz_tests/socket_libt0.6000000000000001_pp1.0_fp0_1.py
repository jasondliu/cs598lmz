import socket
+from uuid import getnode as get_mac
+
+
+def get_ip():
+    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
+    try:
+        # doesn't even have to be reachable
+        s.connect(('10.255.255.255', 1))
+        IP = s.getsockname()[0]
+    except:
+        IP = '127.0.0.1'
+    finally:
+        s.close()
+    return IP
+
+
+def get_mac_address():
+    mac = get_mac()
+    return ':'.join(("%012X" % mac)[i:i + 2] for i in range(0, 12, 2))
+
+
+def get_hostname():
+    return socket.gethostname()
+
+
+def get_system():
+    return platform.system()
+
+
+def get_version():
+    return platform.version()
+
+
+

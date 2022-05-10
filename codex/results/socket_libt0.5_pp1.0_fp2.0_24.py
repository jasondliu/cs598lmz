import socket
+import ipaddress
+
+
+def check_ip(ip):
+    try:
+        ipaddress.ip_address(ip)
+        return True
+    except ValueError:
+        return False
+
+
+def check_port(port):
+    try:
+        port = int(port)
+        if port >= 0 and port <= 65535:
+            return True
+        else:
+            return False
+    except ValueError:
+        return False
+
+
+def is_open(host, port):
+    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+    s.settimeout(0.5)
+    try:
+        s.connect((host, port))
+        s.shutdown(socket.SHUT_RDWR)
+        return True
+    except socket.error:
+        return False
+    finally:
+        s.close()
+
+
+def main():
+    ip = input("Enter ip address: ")


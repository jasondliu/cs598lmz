import socket
+
+
+def get_ip_address():
+    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
+    s.connect(("8.8.8.8", 80))
+    return s.getsockname()[0]
+
+
+def get_mac_address():
+    return ':'.join(re.findall('..', '%012x' % uuid.getnode()))
+
+
+def get_hostname():
+    return socket.gethostname()
+
+
+def get_machine_info():
+    return {
+        'ip_address': get_ip_address(),
+        'mac_address': get_mac_address(),
+        'hostname': get_hostname()
+    }
+
+
+def get_cpu_info():
+    return {
+        'cpu_count': psutil.cpu_count(),
+        'cpu_percent': psutil.cpu_percent(),
+        'cpu_freq': psutil.

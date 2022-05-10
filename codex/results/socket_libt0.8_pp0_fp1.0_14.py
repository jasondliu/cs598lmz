import socket
+import struct
+import time
+from datetime import datetime
+
+# Getting current time reference
+NTP_TIME = 2208988800
+
+
+# Getting the time and comparing with reference
+def ntp_time(host="pool.ntp.org"):
+    try:
+        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
+        client.settimeout(3)
+        data = '\x1b' + 47 * '\0'
+        client.sendto(data.encode(), (host, 123))
+        data, address = client.recvfrom(1024)
+        if data:
+            t = struct.unpack('!12I', data)[10]
+            t -= NTP_TIME
+            return datetime.utcfromtimestamp(t).strftime('%H:%M:%S')
+    except:
+        return "ERR"
+
+
+# Displaying time
+def display_time():
+    print("\

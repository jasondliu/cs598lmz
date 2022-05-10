import _struct
+
+def get_ip_address(hostname):
+    return socket.gethostbyname(hostname)
+
+def get_port_number(name):
+    return socket.getservbyname(name, 'tcp')
+
+def resolve_hostname(hostname):
+    try:
+        nums = socket.gethostbyname_ex(hostname)[2]
+    except:
+        return "<Not Found>"
+    return ", ".join(nums)
+
+def resolve_ip(ip):
+    try:
+        hostname = socket.gethostbyaddr(ip)[0]
+    except:
+        return "<Not Found>"
+    return hostname
+
+def ping(time):
+    time = time * 1000
+    hostname = raw_input("Enter hostname/IP: ")
+    dest = get_ip_address(hostname)
+
+    print "PING %s (%s): %d bytes of data." % (hostname, dest, data_size)
+   

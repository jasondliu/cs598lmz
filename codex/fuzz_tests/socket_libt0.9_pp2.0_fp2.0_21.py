import socket
+
+sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
+sock.bind(('0.0.0.0',22222))
+
+while True:
+    (data, addr) = sock.recvfrom(1024)
+    print "Received from %s." % (addr,)
+    print " -> %s" % (data,)


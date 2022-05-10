import socket
+import os
+import sys
+from struct import *
+
+#create and bind a socket, then run the sniffer
+def run():
+    #create a socket
+    try:
+        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
+    except socket.error, msg:
+        print "Socket could not be created. Error Code: " + str(msg[0]) + " Message " + msg[1]
+        sys.exit()
+
+    #bind socket to public interface
+    s.bind(("", 0))
+    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
+
+    #include IP headers
+    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
+
+    #receive packets
+    while True:
+        raw_buffer = s.recvfrom(65565)
+        ipheader = IP(raw_buffer[0

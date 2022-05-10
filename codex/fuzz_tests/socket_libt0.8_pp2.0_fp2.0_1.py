import socket
+import os
+
+#load server config
+cfg = open('rtsp_server.cfg','r')
+lines = cfg.readlines()
+cfg.close()
+
+#rtp port
+rtpPort = int(lines[0].split(':')[1])
+
+#dir to store uploaded files
+dir = lines[1].split(':')[1].strip('\n')
+
+#create socket
+rtpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
+rtpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
+rtpSocket.bind(('',rtpPort))
+
+while True:
+    data,address = rtpSocket.recvfrom(2048)
+    if (data):
+        print address
+        print data
+
+
+
+


import socket
+import time
+
+# set up the UDP socket
+UDP_IP = "192.168.1.1"
+UDP_PORT = 8899
+sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
+
+
+def get_distance():
+    #sends a request to the drone to get the distance to the ground
+    MESSAGE = "\xcc\xab\xaa\xaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
+    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
+    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
+    print "received message:", data
+
+
+def takeoff():
+    # sends a request to the drone to take off
+    MESSAGE = "\xcc\xab\xaa\xaa\x01\x00\x00

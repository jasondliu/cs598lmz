import socket, sys, re
+
+# Input validation
+if len(sys.argv) < 3:
+    print "Usage: ", sys.argv[0], " <HOST> <PORT>"
+    sys.exit(1)
+
+host = sys.argv[1] 
+port = int(sys.argv[2])
+
+s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+
+try:
+    print "Connecting to ", host, ":", port
+    s.connect((host, port))
+    print "Connected to ", host, ":", port
+except socket.error as msg:
+    print "Could not connect to: ", host, ":", port
+    print "Error: ", msg[0], ":", msg[1]
+    sys.exit(1)
+
+
+# Input validation
+if len(sys.argv) < 2:
+    print "Usage: ", sys.argv[0], " <FILE>"
+    sys.

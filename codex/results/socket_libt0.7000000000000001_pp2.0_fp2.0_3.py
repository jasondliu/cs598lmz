import socket
+import threading
+import time
+
+def TCP_connect(ip,port_number,delay,counter):
+	TCP_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+	TCP_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
+	TCP_sock.settimeout(delay)
+	try:
+		TCP_sock.connect((ip, port_number))
+		print ("Port", port_number, "is open")
+		TCP_sock.close()
+	except:
+		print ("Port", port_number, "is not open")
+		counter += 1
+
+# Get host
+host = input("Enter a remote host to scan: ")
+ip = socket.gethostbyname(host)
+
+# Print a nice banner with information on which host we are about to scan
+print ("-" * 60)
+print ("Please wait, scanning remote host

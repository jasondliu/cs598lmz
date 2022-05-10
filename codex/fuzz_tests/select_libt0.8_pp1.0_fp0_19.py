import select
+
+import RPi.GPIO as GPIO
+
+GPIO.setmode(GPIO.BOARD)
+GPIO.setup(11, GPIO.OUT)
+GPIO.setup(13, GPIO.OUT)
+GPIO.setup(15, GPIO.OUT)
+
+# Set the socket functions to use te de0 nano names
+host = "de0_nano_1"
+port = 2332
+backlog = 5
+size = 1024
+s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
+s.bind((host,port))
+s.listen(backlog)
+input = [s,sys.stdin]
+
+while 1:
+    inputready,outputready,exceptready = select.select(input,[],[])
+
+    for i in inputready:
+
+        if i == s:
+            # handle the server socket
+           

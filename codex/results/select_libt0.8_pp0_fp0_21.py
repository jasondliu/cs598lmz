import select
+
+s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+s.settimeout(2)
+# connect to remote host
+try:
+    s.connect((host, port))
+except socket.gaierror, e:
+    print 'Hostname could not be resolved. Exiting'
+    sys.exit()
+print 'Socket Connected to ' + host + ' on ip ' + hostaddr
+
+# read data
+try:
+    s.sendall('X' + sys.argv[2])
+    while 1:
+        r, w, e = select.select([s], [], [])
+        if r:
+            msg = s.recv(4096)
+            print msg
+except socket.error, e:
+    print 'Send failed'
+    sys.exit()
+
+s.close()


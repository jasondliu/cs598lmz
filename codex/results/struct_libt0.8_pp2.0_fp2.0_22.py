import _struct
+
+s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
+s.bind(('', 10110))
+
+while True:
+    try:
+        message, address = s.recvfrom(8192)
+    except socket.error:
+        print "Error!"
+        sys.exit()
+    else:
+        print "Got data from", address
+        (counter, mac1, mac2, mac3, mac4, mac5, mac6) = _struct.unpack('>HBBBBBB', message[:8])
+        print 'counter:', counter, 'mac:', mac1, mac2, mac3, mac4, mac5, mac6
+        print 'Bytes:', [hex(ord(c)) for c in message[8:]]
+        s.sendto(message, address)


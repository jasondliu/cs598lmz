import _struct
+
+# Convert a string of 6 characters of ethernet address into a dash separated hex string
+def eth_addr (a) :
+  b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
+  return b
+
+# Create a AF_PACKET type raw socket (thats basically packet level)
+# define ETH_P_ALL    0x0003          /* Every packet (be careful!!!) */
+try:
+    s = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))
+except socket.error , msg:
+    print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
+    sys.exit()
+
+# receive a packet
+while True:
+

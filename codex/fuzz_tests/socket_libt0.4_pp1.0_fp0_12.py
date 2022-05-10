import socket
+import sys
+
+def get_constants(prefix):
+    """Create a dictionary mapping socket module constants to their names."""
+    return dict( (getattr(socket, n), n)
+                 for n in dir(socket)
+                 if n.startswith(prefix)
+                 )
+
+families = get_constants('AF_')
+types = get_constants('SOCK_')
+protocols = get_constants('IPPROTO_')
+
+# Create a TCP/IP socket
+sock = socket.create_connection(('localhost', 10000))
+
+print >>sys.stderr, 'Family  :', families[sock.family]
+print >>sys.stderr, 'Type    :', types[sock.type]
+print >>sys.stderr, 'Protocol:', protocols[sock.proto]
+print >>sys.stderr
+
+try:
+    
+    # Send data
+    message = 'This is the message.  It will be repeated.'

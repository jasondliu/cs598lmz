import socket
+
+server_address = './uds_socket'
+
+# Make sure the socket does not already exist
+try:
+    os.unlink(server_address)
+except OSError:
+    if os.path.exists(server_address):
+        raise
+
+# Create a UDS socket
+sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
+
+# Bind the socket to the port
+print >>sys.stderr, 'starting up on %s' % server_address
+sock.bind(server_address)
+
+# Listen for incoming connections
+sock.listen(1)
+
+while True:
+    # Wait for a connection
+    print >>sys.stderr, 'waiting for a connection'
+    connection, client_address = sock.accept()
+    try:
+        print >>sys.stderr, 'connection from', client_address
+
+        # Receive the data in small chunks and retransmit it
+

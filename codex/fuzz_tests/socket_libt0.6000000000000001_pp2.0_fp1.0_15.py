import socket
+import sys
+
+
+# Get the server hostname and port as command line arguments                    
+host = sys.argv[1]
+port = int(sys.argv[2])
+
+# Create a UDP socket
+# Notice the use of SOCK_DGRAM for UDP packets
+try:
+    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
+    print('Socket created')
+except socket.error as err:
+    print('socket open error: {}\n'.format(err))
+    exit()
+
+
+# Send data
+msg = 'This is the message.  It will be repeated.'
+
+try:
+    # Set the total message parts
+    total = 1
+
+    # Send the data through the socket
+    print('sending {!r}'.format(msg))
+    s.sendto(msg.encode(), (host, port))
+
+    # Look for the response
+    print('waiting to receive')
+   

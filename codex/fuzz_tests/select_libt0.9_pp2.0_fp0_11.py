import select
+
+def write_to_socket(socket, data):
+    try:
+        socket.send(data)
+        return True
+    except socket.error, e:
+        print 'Error on write: %s' % str(e)
+        return False
+    
+def read_from_socket(socket, max_len_bytes=1024, timeout=0.5):
+    """
+    Perform a blocking read on a socket, with a timeout specified.
+    """
+    data = ''
+    readable, _, _ = select.select([socket], [], [], timeout)
+    if readable:
+        data = socket.recv(max_len_bytes)
+    return data


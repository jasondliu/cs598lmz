import select
+
+
+server = socket.socket()
+server.bind(('localhost', 9000))
+server.listen(1)
+
+connection, adress = server.accept()
+
+
+while True:
+
+    rlist = [connection]
+    wlist = []
+    xlist = []
+
+    readable, writable, exceptional = select.select(rlist, wlist, xlist)
+
+    for r in readable:
+        print(connection.recv(4096).decode('utf-8'))
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+

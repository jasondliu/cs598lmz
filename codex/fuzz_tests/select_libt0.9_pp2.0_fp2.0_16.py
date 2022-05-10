import select, socket, sys
+
+
+port = 12345
+size = 1024
+s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+s.bind(('localhost',port))
+s.listen(5)
+
+inputs = [s]
+
+running = 1
+
+while running:
+  try:
+    inputready,outputready,exceptready = select.select(inputs,[],[])
+  except KeyboardInterrupt:
+    print("Exiting")
+    running = 0
+  for s in inputready:
+    if s == server:
+      client, address = s.accept()
+      print("New connection from: " + address[0])
+      inputs.append(client)
+    else:
+      try:
+        data = s.recv(size)
+        if data:
+          s.send(data)
+        else:
+          print("Closing connection")
+          s.close()
+          inputs.remove(s)
+

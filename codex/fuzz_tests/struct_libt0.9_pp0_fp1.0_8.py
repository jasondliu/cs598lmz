import _struct
+from threading import Timer
+from functools import partial
+
+def listen(server, client, address):
+  try:
+    message = client.recv(200)
+    if message:
+      msg = message.strip().split(b' ')
+      if msg[0] == b'PING':
+        client.send(bytes(b'PONG ' + msg[1] + b'\r\n', 'utf-8'))
+    else:
+      raise Exception('client disconnected')
+  except:
+    client.close()
+    server.connections.discard(client)
+    return
+
+  Timer(0.01, partial(listen, server, client, address), ()).start()
+
+class kelpdark(threading.Thread):
+  def __init__(self, server, address, port):
+    super(kelpdark, self).__init__()
+    self.connections = set()
+    self.server = server
+    self.port = port

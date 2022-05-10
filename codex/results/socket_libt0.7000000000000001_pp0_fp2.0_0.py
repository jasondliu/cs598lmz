import socket
+import threading
+
+
+def receive(client, username):
+    while True:
+        try:
+            message = client.recv(1024).decode('ascii')
+            if message == 'NICK':
+                client.send('NICK'.encode('ascii'))
+                username = client.recv(1024).decode('ascii')
+                message = username + ' has joined the chat!'
+                broadcast(message, client)
+                print(username + ' has joined the chat!')
+            else:
+                print(message)
+                message_to_send = "<" + username + "> " + message
+                broadcast(message_to_send, client)
+        except:
+            client.close()
+            remove(client)
+            return
+
+
+def broadcast(message, connection):
+    for client in clients:
+        if client != connection:
+            try:
+                client.send(message.encode('ascii'))
+            except:


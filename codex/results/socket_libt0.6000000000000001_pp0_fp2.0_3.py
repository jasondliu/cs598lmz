import socket
+import argparse
+import threading
+
+parser = argparse.ArgumentParser(description='This is a simple TCP server')
+parser.add_argument('--port', '-p', type=int, required=True, help='Port to listen on')
+args = parser.parse_args()
+
+bind_ip = ''
+bind_port = args.port
+
+server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+server.bind((bind_ip, bind_port))
+server.listen(5)
+
+print('[*] Listening on %s:%d' % (bind_ip, bind_port))
+
+# this is our client-handling thread
+def handle_client(client_socket):
+    # print out what the client sends
+    request = client_socket.recv(1024)
+    print('[*] Received: %s' % request)
+
+    # send back a packet
+    client_socket.send(b'ACK!')


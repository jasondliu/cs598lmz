import socket
+import pickle
+import threading
+import time
+
+
+def send(sock, msg):
+    data = pickle.dumps(msg)
+    sock.send(data)
+
+
+def recv(sock):
+    data = sock.recv(1024)
+    msg = pickle.loads(data)
+    return msg
+
+
+def recv_thread(sock):
+    while True:
+        msg = recv(sock)
+        print(msg)
+
+
+def main():
+    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+    sock.connect(('127.0.0.1', 9090))
+    send(sock, 'Hello')
+
+    thread = threading.Thread(target=recv_thread, args=(sock,))
+    thread.start()
+
+    while True:
+        msg = input()
+        send(sock, msg)
+
+

import socket
+from threading import Thread
+
+def receive(sock):
+    while True:
+        msg = sock.recv(2048).decode('utf-8')
+        print(msg)
+
+def main():
+    host = '127.0.0.1'
+    port = 5000
+
+    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+    sock.connect((host, port))
+
+    receive_thread = Thread(target=receive, args=(sock, ))
+    receive_thread.start()
+
+    while True:
+        msg = input()
+        sock.send(msg.encode('utf-8'))
+
+if __name__ == '__main__':
+    main()


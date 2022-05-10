import socket
+
+def main():
+
+    host = '127.0.0.1'
+    port = 5000
+
+    server = ('127.0.0.1', 5001)
+
+    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
+    s.bind((host, port))
+
+    message = input("-> ")
+    while message != 'q':
+        s.sendto(message.encode, server)
+        data, addr = s.recvfrom(1024)
+        data = data.decode()
+        print("Received from server: " + data)
+        message = input("-> ")
+    s.close()
+
+if __name__ == '__main__':
+    main()


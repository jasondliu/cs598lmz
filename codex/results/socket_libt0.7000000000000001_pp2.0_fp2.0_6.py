import socket
+import threading
+import sys
+
+def main():
+    if len(sys.argv) != 3:
+        print ("Correct usage: script, IP address, port number")
+        exit()
+    IP_address = str(sys.argv[1])
+    Port = int(sys.argv[2])
+    server = ('127.0.0.1', 5000)
+
+    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
+    s.bind((IP_address, Port))
+
+    msg = input("-> ")
+    while msg != 'q':
+        s.sendto(msg.encode(), server)
+        data, addr = s.recvfrom(1024)
+        print("Received from server: " + str(data.decode()))
+        msg = input("-> ")
+    s.close()
+
+if __name__ == '__main__':
+    main()


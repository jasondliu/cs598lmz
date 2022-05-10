import socket
+import threading
+
+
+def main():
+    global serverSocket
+
+    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
+    serverSocket.bind((socket.gethostname(), 8080))
+    serverSocket.listen(10)
+
+    while True:
+        clientSocket, clientAddress = serverSocket.accept()
+        threading.Thread(target=clientThread, args=(clientSocket, clientAddress)).start()
+
+
+def clientThread(clientSocket, clientAddress):
+    acceptedMessage = clientSocket.recv(1024)
+
+    print("{0} has sent: {1}".format(clientAddress, acceptedMessage))
+
+    clientSocket.sendall(b"This is from the server!")
+    clientSocket.close()
+
+
+if __name__ == "__main__":
+    main()


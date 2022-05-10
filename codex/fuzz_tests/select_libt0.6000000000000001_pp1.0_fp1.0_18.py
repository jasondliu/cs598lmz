import select
+
+# Set up server socket
+server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+server_socket.bind(("0.0.0.0", 5000))
+server_socket.listen()
+
+# Add server socket to the list of readable connections
+CONNECTION_LIST.append(server_socket)
+
+print("Chat server started on port " + str(5000))
+
+while 1:
+    # Get the list sockets which are ready to be read through select
+    read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
+
+    for sock in read_sockets:
+        #New connection
+        if sock == server_socket:
+            # Handle the case in which there is a new connection recieved through server_socket
+            sockfd, addr = server_socket.accept()
+            CONNECTION_LIST.append(sockfd)
+            print("Client (%s, %s) connected" % addr)

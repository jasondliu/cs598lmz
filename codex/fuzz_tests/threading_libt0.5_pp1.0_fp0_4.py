import threading
threading.Thread(target=start_server).start()

#Now you can use your browser to connect to the server at port 8080.
#You can also use telnet or netcat to connect to the server.
#For example, if you use telnet, you can start the telnet client and then connect to the server:
#telnet 127.0.0.1 8080
#You will see the following output:
#Trying 127.0.0.1...
#Connected to 127.0.0.1.
#Escape character is '^]'.
#Hello World!
#Connection closed by foreign host.
#You can see the server sent the message "Hello World!" to the client.
#The client received the message and then closed the connection.
#You can also use netcat to connect to the server:
#nc 127.0.0.1 8080
#You will see the following output:
#Hello World!
#You can see the server sent the message "Hello World!" to the client.
#The client received the message and then closed the connection.
#You can connect to the server using your browser

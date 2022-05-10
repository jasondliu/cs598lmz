import socket
socket.if_indextoname(3)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
s.getsockname()
try:
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # create a socket object
        host = socket.gethostname()  # get local machine name
        port = 6789  # reserve a port for your service every new transfer wants a new port or you must wait.
        s.bind((host, port))  # bind to the port
        # Receive no more than 1024 bytes

        message = s.recv(1024).decode("utf-8")
        print("Message form client " + message)
        s.close()
except KeyboardInterrupt:
    print("Good bye")

##Servidor
import os, sys
import socket

s = socket.socket()
host = socket.gethostname()
print("server will start on host : ", host)
port = 12345
s.bind

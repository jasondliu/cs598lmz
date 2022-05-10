import socket
import sys
import base64
import threading
import multiprocessing

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

def handle_client(clientsocket):
    print("Accepted connection from: ", clientsocket.getpeername())
    #print(clientsocket.getpeername())
    while True:
        msg = clientsocket.recv(2048)
        #print("Received: ", msg)
        if not msg:
            break
        print("Received: ", msg.decode("utf-8"))
        msg_decoded = msg.decode("utf-8")
        if msg_decoded == "exit":
            break;
        if msg_decoded == "forward":
            print("Moving forward")

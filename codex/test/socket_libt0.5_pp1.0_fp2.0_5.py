import socket
import threading

host = "127.0.0.1"
port = 8080

#creating the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#binding the server to the localhost and the port
server.bind((host,port))

#listening to the server
server.listen(1)

#creating a list of clients
clients = []

#creating a list of locks
locks = []

#create a lock for each client
for i in range(10):
    locks.append(threading.Lock())

#function for handling the client
def handle_client(client):
    #the client sends a name
    name = client.recv(1024).decode("utf8")
    #welcome message
    welcome = "Welcome %s! If you want to quit, type {quit} to exit!" % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name

import socket
from datetime import datetime
from threading import Thread

# date and time
date = datetime.now()
print("Date: ", date.strftime("%d/%m/%Y"))
print("Time: ", date.strftime("%H:%M"))

LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsocket, clientAddress = server.accept()
    print("Connected to : ", clientAddress)
    message = "thank you for connecting"
    clientsocket.send(message.encode())
    clientsocket.close()

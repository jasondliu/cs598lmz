import socket
import random
import sys

#Define the socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Print our IP and Port
print("Your IP and Port are: ")
print(socket.gethostbyname(socket.gethostname()))
print(s.getsockname()[1])

#Set our flag for the main loop
s.setblocking(0)

#We need to know the address and port of the client, duh
address = input("Enter the address of the client: ")
port = int(input("Enter the PORT of the client: "))

#Initilize the game loop
playing = True

while playing:
    #Recieve the message, if there is one
    try:
        message, serverAddress = s.recvfrom(1024)
        print("Message from ", serverAddress, ": ", message.decode())
    except socket.error:
        pass
    
    #Get our input
    message = input("Message: ")
    if message == "quit":
        playing

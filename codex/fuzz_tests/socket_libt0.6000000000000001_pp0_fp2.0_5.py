import socket
from sys import argv
from struct import *

#define the ip address and port number of the server
ip = '127.0.0.1'
port = 12345

# create a socket for the client
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
clientsocket.connect((ip, port))

#get the filename and the mode from the command line arguments
filename = argv[1]
mode = argv[2]

# send the filename and mode
clientsocket.send(filename.encode())
clientsocket.send(mode.encode())

# get the response from the server
response = clientsocket.recv(1)

# if the response is 1 then the file is present
if response.decode() == '1':
    # get the file size from the server
    filesize = clientsocket.recv(4)
    filesize = unpack('!L', filesize)[0]

    # get the file from the server
    data = clientsocket.recv

import socket
import threading
import os
import os.path
import sys
import time



# Get the server hostname and port as command line arguments
def getArguments():
    argList = sys.argv
    if len(argList) < 3:
        print('Usage: python FTPclient.py server-host-name server-port')
        sys.exit(1)
    return argList[1], int(argList[2])


# Create socket and connect to server
def createSocket(hostName, port):
    # Create TCP client socket. Note the use of SOCK_STREAM for TCP packet
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to server address
    clientSocket.connect((hostName, port))
    return clientSocket


# Create a new socket for file transfer
def createDataSocket():
    # Create TCP client socket. Note the use of SOCK_STREAM for TCP packet
    dataSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return dataSocket



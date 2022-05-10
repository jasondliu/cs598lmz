import socket
import sys
import os
import shutil
import time
import threading
import string
import random

#Global variables

#server_address = ('localhost', 10000)
server_address = ('192.168.1.4', 10000)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect the socket to the port where the server is listening
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

#Create a new directory for the client

directory = 'client'

if not os.path.exists(directory):
    os.makedirs(directory)

#Set the current directory to the new one

os.chdir(directory)

#Function to receive a file from the server
def receive_file(filename):
    #Receive the file size
    file_size = sock.recv(1024)
    file_size = int(file_size)
    print >>sys.stderr, 'Receiving %s

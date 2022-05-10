import socket
import threading
import os
import sys

#----- Global Variables -----#

#----- Functions -----#

#----- Main Code -----#

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Create a list of files in the current directory
file_list = os.listdir()

# Send the list of files to the client
for file in file_list:
	sock.sendto(file.encode(), ('localhost', 10001))

# Close the socket
sock.close()

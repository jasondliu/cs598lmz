import socket
import time

# Define the target
target_name = "<Target Name Here>"
target_ip = "<Target IP Here>"

# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (target_ip, 22)

# Connect the socket to the port where the server is listening
print('connecting to %s port %s' % server_address)
s.connect(server_address)
time.sleep(1)

# Receive the banner
banner = s.recv(512)

import socket
import struct
import sys

# The IP address or hostname of the server, and the port number to use
server = ('10.0.0.1', 9000)

# How many bytes to send in each request
BUFFER_SIZE = 4096

# The number of requests to make
REQUESTS = 100

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send the requests
for i in range(REQUESTS):
    # Send a request
    sock.sendto(struct.pack('>I', i), server)

    # Wait for a response
    data, address = sock.recvfrom(BUFFER_SIZE)

    # Print the response
    print(str(i) + ' ' + data)

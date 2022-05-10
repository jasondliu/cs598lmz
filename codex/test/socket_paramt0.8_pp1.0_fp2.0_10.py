import socket
socket.if_indextoname(6)

socket.if_nameindex()

socket.if_nametoindex('Loopback Pseudo-Interface 1')

socket.gethostbyname('www.google.com')

socket.gethostbyname_ex('www.google.com')

socket.gethostbyaddr('74.125.235.240')

# Simple client-server with UDP
import socket
import sys

# Create a UDP/IP socket
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('Starting up on {} port {}'.format(*server_address))
sock2.bind(server_address)

while True:
    print('\nWaiting to receive message')
    data, address = sock2.recvfrom(4096)

    print('Received {} bytes from {}'.format(
        len(data), address
    ))
    print(data)

    if data:
        sent = sock2.sendto(data, address)


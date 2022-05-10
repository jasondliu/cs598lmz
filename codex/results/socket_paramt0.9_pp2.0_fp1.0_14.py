import socket
socket.if_indextoname(2)

# Go through the NIC descriptions and find the one that isn't the loopback interface
for i, desc in enumerate(socket.if_nameindex()):
    if 'lo' not in desc:
        print(desc)

# Set the last parameter to True to turn on promiscuous mode
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
# Receive 512 bytes at a time
print(s.recvfrom(512))

'''
There are better ways to send data out over the network than creating our own packets and sending them via raw sockets. Python provides a couple of ways to do that for us:

1. The more low-level way is to use the socket module, which we just talked about. The socket module contains standard calls for a wide variety of socket-related functions and actions. These include raw sockets and some simple functions for sending ICMP messages like ping.

2. There is another module, the socket_io module, that is a wrapper around the socket module. It provides a higher-level interface (similar to stream I/O

import socket
socket.if_indextoname(1)

# 'lo0'

# if_indextoname() is the inverse of if_nametoindex().

# Socket Type

# SOCK_STREAM and SOCK_DGRAM are the two most common types.

# TCP/IP socket

# A socket is a named endpoint for network traffic. It is a handle for sending and receiving data. A socket has an address,
# composed of the network address and a port number, and a type, which identifies the transport layer protocol.

# A socket is created using the socket() function.

# The socket() function takes the address family, socket type, and protocol number as arguments.

# import socket
# socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0>

# The address family specifies the protocol family used by the socket.
# This is typically AF_INET for IPv4, but may be another protocol depending on the address family supported by the operating system

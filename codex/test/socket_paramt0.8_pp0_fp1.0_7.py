import socket
socket.if_indextoname(3)

import socket
socket.if_nameindex()

import socket
socket.if_nametoindex('lo0')

import socket
socket.getaddrinfo('www.python.org', 'http')

import socket
socket.getaddrinfo('127.0.0.1', 8080)

import socket
socket.getaddrinfo('127.0.0.1', 8080, 0, 0, socket.IPPROTO_TCP)

import socket
def get_constants(prefix):
    """Create a dictionary mapping socket module constants to their names."""
    return dict( (getattr(socket, n), n)
                 for n in dir(socket)
                 if n.startswith(prefix)
                 )

protocols = get_constants('IPPROTO_')

for name in ['icmp', 'udp', 'tcp']:
    proto_num = socket.getprotobyname(name)
    const_name = protocols[proto_num]

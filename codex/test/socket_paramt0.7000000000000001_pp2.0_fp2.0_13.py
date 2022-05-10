import socket
socket.if_indextoname(1)

socket.if_indextoname(4)

socket.if_indextoname(6)

socket.if_nametoindex('lo0')

socket.if_nametoindex('lo0')

socket.if_nameindex()

socket.if_nameindex()

name = 'lo0'
flags  = socket.IFF_UP | socket.IFF_BROADCAST | socket.IFF_LOOPBACK
addr = socket.inet_aton('127.0.0.1')
netmask = socket.inet_aton('255.255.255.0')
broadaddr = socket.inet_aton('127.0.0.255')
dstaddr = socket.inet_aton('127.0.0.1')

name = 'lo0'
flags  = socket.IFF_UP | socket.IFF_BROADCAST | socket.IFF_LOOPBACK
addr = socket.inet_aton('127.0.0.1')
netmask = socket.inet_aton('255.255.255.0')

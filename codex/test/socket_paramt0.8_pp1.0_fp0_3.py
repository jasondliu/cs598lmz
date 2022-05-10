import socket
socket.if_indextoname(1)

#To get the ip address of a network interface
socket.if_nameindex()
socket.if_nameindex()[1][1]

#To get the ip address of a host
socket.gethostbyname('localhost')
socket.gethostbyname_ex('localhost')

#To get the ip address of a host
socket.gethostbyaddr('127.0.0.1')
socket.gethostbyaddr('127.0.0.1')[2]

#To get the service of a port
socket.getservbyname('http')

#To get the service of a port
socket.getservbyport(80)

#To send a broadcast message
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.sendto(b'Hello World', ('<broadcast>', 24444))

#To create a TCP/IP Server
import socket

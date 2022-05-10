import socket
socket.if_indextoname(10)

#get node name
socket.getfqdn('www.decker.com')

# get ip of the node
socket.gethostbyname('www.decker.com')

# null
socket.gethostbyname_ex('www.decker.com')

#get all ip addrs of a node
socket.gethostbyname_ex('www.decker.com')[2]

#get name of the interface
socket.gethostbyaddr('127.0.0.1')

#get ip address of the interface
socket.gethostbyaddr('127.0.0.1')[2]

#get the nameserver of the node
socket.gethostbyname_ex('www.decker.com')[1]

# get all information about a node
socket.getaddrinfo('www.decker.com', 80)

#get all interfaces
socket.if_indextoname(10)

#get service protocl of a service
socket.getservbyname('http')

#get port of a service
socket.gets

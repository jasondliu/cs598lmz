import socket
socket.if_indextoname(3)

#if_nameindex()
#returns a list of tuples containing interface name and index
socket.if_nameindex()

#if_nametoindex()
#returns the index of the interface with the given name
socket.if_nametoindex('eth0')

#gethostbyaddr()
#returns the host name and the IP address
socket.gethostbyaddr('127.0.0.1')

#gethostbyname()
#returns the IP address of the host with the given name
socket.gethostbyname('localhost')

#gethostbyname_ex()
#returns the IP address and the aliases of the host with the given name
socket.gethostbyname_ex('localhost')

#gethostname()
#returns the host name of the current machine
socket.gethostname()

#getprotobyname()
#returns the protocol number for the given protocol name
socket.getprotobyname('tcp')

#getservbyname()
#returns the port number for the given service name
socket.getserv

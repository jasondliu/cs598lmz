import socket
socket.if_indextoname(3)

#returns the name of the interface with the given index

#socket.if_nameindex()
#returns a list of tuples (index, name) for all interfaces

#socket.if_nametoindex(name)
#returns the index of the interface with the given name

#socket.gethostbyname(name)
#returns the IP address of the given hostname

#socket.gethostname()
#returns the hostname of the current machine

#socket.gethostbyaddr(ip)
#returns a tuple (hostname, [alias, ...], [ip, ...]) for the given IP address

#socket.getnameinfo(sockaddr, flags)
#returns a tuple (host, port) for the given sockaddr

#socket.getprotobyname(name)
#returns the protocol number for the given protocol name

#socket.getservbyname(servicename, protocolname)
#returns the port number for the given service and protocol

#socket.getservbyport(port, protocolname)
#returns

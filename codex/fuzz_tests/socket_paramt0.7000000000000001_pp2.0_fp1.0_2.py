import socket
socket.if_indextoname(2)

socket.if_nameindex()

socket.if_freenameindex(nameindex)

socket.if_nametoindex('en0')

socket.getaddrinfo(host, port, family=0, type=0, proto=0, flags=0)

socket.getnameinfo(sockaddr, flags)

socket.getfqdn(name='')

socket.gethostbyname(hostname)

socket.gethostbyname_ex(hostname)

socket.gethostbyaddr(ip_address)

socket.gethostname()

socket.getprotobyname(protocolname)

socket.getservbyname(servicename, protocolname)

socket.getservbyport(port, protocolname)

#========================================
#    Socket Objects
#========================================

#Create a new socket using the given address family, socket type, and protocol number.

socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)

#family:
#

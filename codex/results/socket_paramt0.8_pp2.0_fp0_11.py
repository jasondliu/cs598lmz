import socket
socket.if_indextoname(4)

# if_nametoindex(interface) converts an interface name into an index
socket.if_nametoindex('eth0')

# getprotobyname(protocol) converts a protocol name into its corresponding protocol number
socket.getprotobyname('tcp')
socket.getprotobyname('udp')

# getprotobynumber(number) converts a number into the corresponding protocol name
socket.getprotobynumber(6)
socket.getprotobynumber(17)

# getservbyname(protocol, port) converts a port name into its numerical port
socket.getservbyname('ftp', 'tcp')

# getservbyport(port, protocol) converts a port number into a name
socket.getservbyport(21, 'tcp')

# htons(port) takes a numerical port and converts it into an integer
socket.htons(21)

# htonl(ip) takes an IP address and converts it into an integer
socket.htonl(2130706433)

# ntohs(integer)

import socket
socket.if_indextoname(1)

# if_nameindex()
# Return a list of tuples containing interface name and index.
socket.if_nameindex()

# if_nametoindex(if_name)
# Translate an interface name to an interface index.
socket.if_nametoindex('lo')

# gethostbyname(hostname)
# Return the IP address (a string) for a host.
socket.gethostbyname('localhost')

# gethostbyaddr(ip_address)
# Return the host name (a string) for an IP address.
socket.gethostbyaddr("127.0.0.1")

# gethostname()
# Return the current host name.
socket.gethostname()

# getprotobyname(protocol_name)
# Return the protocol number for the named protocol.
socket.getprotobyname('tcp')

# getservbyname(service_name[, protocol_name])
# Return a port number for the named service.
socket.getservbyname('ssh')

# getservbyport(port[, protocol

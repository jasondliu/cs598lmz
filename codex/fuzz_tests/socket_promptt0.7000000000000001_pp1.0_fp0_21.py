import socket
# Test socket.if_indextoname()
# Output is None or the interface name

print(socket.if_indextoname(1))

# Test socket.if_nametoindex(if_name)
# Output is None or the index of the interface

print(socket.if_nametoindex('eth0'))

# Test socket.getaddrinfo(host, port[, family[, socktype[, proto[, flags]]]])
# Output is a list of five-tuples that contain all the necessary arguments for creating a socket connected to that service

print(socket.getaddrinfo('www.python.org', 80))

# Test socket.gethostname()
# Output is the host name

print(socket.gethostname())

# Test socket.gethostbyname(hostname)
# Output is the IPv4 address of the host

print(socket.gethostbyname('www.python.org'))

# Test socket.gethostbyname_ex(hostname)
# Output is a tuple (name, aliaslist, ipaddrlist)

print(socket.gethostbyname_ex('

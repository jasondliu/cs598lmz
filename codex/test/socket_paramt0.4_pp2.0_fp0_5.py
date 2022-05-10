import socket
socket.if_indextoname(1)

# socket.if_nameindex()
# Return a list of tuples containing all available interfaces. Each tuple contains the interface index and the interface name.

socket.if_nameindex()

# socket.if_nametoindex(if_name)
# Return the interface index for the interface which has the given name.

socket.if_nametoindex('lo')

# socket.getaddrinfo(host, port, family=0, type=0, proto=0, flags=0)
# Translate the host/port argument into a sequence of 5-tuples that contain all the necessary arguments for creating a socket connected to that service.
# host is a domain name, a string representation of an IPv4/v6 address or None. port is a string service name such as 'http', a numeric port number or None.
# By default, socket.getaddrinfo() returns a list of socket address structures that contains IPv4 addresses. To make it return IPv6 addresses, pass AF_INET6 as the value of the family parameter.

socket.getaddrinfo('www.python.org', 'http')

# socket

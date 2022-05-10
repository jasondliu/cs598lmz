import socket
socket.if_indextoname(3)

# get all interfaces
socket.if_nameindex()

# get all addresses
socket.getaddrinfo('www.python.org', 'http')

# get all addresses for a specific family
socket.getaddrinfo('www.python.org', 'http', socket.AF_INET)

# get all addresses for a specific family and type
socket.getaddrinfo('www.python.org', 'http', socket.AF_INET, socket.SOCK_STREAM)

# get all addresses for a specific family, type and protocol
socket.getaddrinfo('www.python.org', 'http', socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

# get all addresses for a specific family, type and protocol
socket.getaddrinfo('www.python.org', 'http', socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, socket.AI_CANONNAME)

# get all addresses for a specific family, type and protocol

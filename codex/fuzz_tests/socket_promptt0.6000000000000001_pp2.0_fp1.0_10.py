import socket
# Test socket.if_indextoname()
socket.if_indextoname(1)

# Test socket.if_nameindex()
socket.if_nameindex()

# Test socket.if_nametoindex()
socket.if_nametoindex('lo')

# Test socket.getaddrinfo()
socket.getaddrinfo('localhost', 8080, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_PASSIVE)
socket.getaddrinfo('localhost', 8080, socket.AF_UNSPEC, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Test socket.getnameinfo()
socket.getnameinfo(('127.0.0.1', 8080), 0)

# Test socket.getfqdn()
socket.getfqdn('localhost')

# Test socket.gethostbyname()
socket.gethostbyname('localhost')

# Test socket.gethostbyname_ex()
socket.gethostbyname_ex('localhost')

# Test socket.gethostbyaddr()
socket.gethostbyaddr('

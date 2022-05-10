import socket
# Test socket.if_indextoname
socket.if_indextoname(1)

# Test socket.if_nameindex
socket.if_nameindex()

# Test socket.if_nametoindex
socket.if_nametoindex(socket.if_indextoname(1))

# Test socket.gethostbyaddr
socket.gethostbyaddr(socket.gethostname())

# Test socket.gethostbyname_ex
socket.gethostbyname_ex(socket.gethostname())

# Test socket.getnameinfo
socket.getnameinfo(('127.0.0.1', 22), 0)

# Test socket.getfqdn
socket.getfqdn(socket.gethostname())

# Test socket.gethostname
socket.gethostname()

# Test socket.gethostbyname
socket.gethostbyname(socket.gethostname())

# Test socket.getservbyname
socket.getservbyname('ssh')

# Test socket.getaddrinfo
socket.getaddrinfo('www.google.com', 80)

# Test socket

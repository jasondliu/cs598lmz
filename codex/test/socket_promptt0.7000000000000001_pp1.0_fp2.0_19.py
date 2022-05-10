import socket
# Test socket.if_indextoname()
socket.if_indextoname(1)

# Test socket.if_nameindex()
socket.if_nameindex()

# Test socket.if_nametoindex()
socket.if_nametoindex('lo')

# Test socket.getaddrinfo()
socket.getaddrinfo('localhost', 'http')

# Test socket.getfqdn()
socket.getfqdn('localhost')

# Test socket.gethostbyaddr()
socket.gethostbyaddr('127.0.0.1')

# Test socket.gethostbyname()
socket.gethostbyname('localhost')

# Test socket.gethostbyname_ex()
socket.gethostbyname_ex('localhost')

# Test socket.gethostname()
socket.gethostname()

# Test socket.getnameinfo()
try:
    socket.getnameinfo(('127.0.0.1', 80), 0)
except socket.gaierror:
    pass

# Test socket.getservbyname()
socket.getservbyname('domain')


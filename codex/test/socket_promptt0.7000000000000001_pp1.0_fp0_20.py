import socket
# Test socket.if_indextoname()
[socket.if_indextoname(i) for i in range(10)]

# Test socket.if_nameindex()
socket.if_nameindex()

# Test socket.if_nametoindex()
[socket.if_nametoindex(i) for i in range(10)]

# Test socket.gethostbyname()
socket.gethostbyname('localhost')

# Test socket.gethostbyname_ex()
socket.gethostbyname_ex('localhost')

# Test socket.gethostbyaddr()
socket.gethostbyaddr('127.0.0.1')

# Test socket.gethostname()
socket.gethostname()

# Test socket.getprotobyname()
socket.getprotobyname('tcp')

# Test socket.getservbyname()
socket.getservbyname('http', 'tcp')

# Test socket.getservbyport()
socket.getservbyport(80, 'tcp')

# Test socket.getaddrinfo()

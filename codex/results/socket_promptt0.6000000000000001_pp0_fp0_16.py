import socket
# Test socket.if_indextoname()
socket.if_indextoname(1)

# Test socket.if_nametoindex()
socket.if_nametoindex('lo')

# Test socket.if_nameindex()
socket.if_nameindex()

# Test socket.if_freenameindex()
socket.if_freenameindex(socket.if_nameindex())

# Test socket.getaddrinfo()
socket.getaddrinfo('localhost', 'http')

# Test socket.getnameinfo()
socket.getnameinfo(socket.getaddrinfo('localhost', 'http')[0][4], 0)

# Test socket.gethostbyname()
socket.gethostbyname('localhost')

# Test socket.gethostbyname_ex()
socket.gethostbyname_ex('localhost')

# Test socket.gethostbyaddr()
socket.gethostbyaddr('127.0.0.1')

# Test socket.getservbyname()
socket.getservbyname('http')

# Test socket.getservbyport()
socket.getservbyport(

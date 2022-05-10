import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(5))

# Test socket.if_nameindex()
print(socket.if_nameindex())

# Test socket.if_nametoindex()
print(socket.if_nametoindex('wlan0'))

# Test socket.getaddrinfo()
print(socket.getaddrinfo('www.python.org', 80))

# Test socket.getfqdn()
print(socket.getfqdn('8.8.8.8'))

# Test socket.gethostbyname()
print(socket.gethostbyname('www.python.org'))

# Test socket.gethostbyname_ex()
print(socket.gethostbyname_ex('www.python.org'))

# Test socket.gethostbyaddr()
print(socket.gethostbyaddr('8.8.8.8'))

# Test socket.gethostname()
print(socket.gethostname())

# Test socket.getnameinfo()
print(socket.getnameinfo(('8.8.8

import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))

# Test getaddrinfo()
# Return a list of 5 tuples for socket.getaddrinfo()
print(socket.getaddrinfo("www.python.org", "http", 0, socket.SOCK_STREAM))

# Test getnameinfo()
# Return a tuple for socket.getnameinfo()
print(socket.getnameinfo(("www.python.org", 80), 0))

# Test getfqdn()
print(socket.getfqdn("8.8.8.8"))

# Test gethostbyname()
print(socket.gethostbyname("www.python.org"))

# Test gethostbyname_ex()
print(socket.gethostbyname_ex("www.python.org"))

# Test gethostbyaddr()
print(socket.gethostbyaddr("207.241.224.2"))

# Test getservbyname()
print(socket.getservbyname("http", "tcp"))

# Test getprotobyname()

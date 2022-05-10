import socket
# Test socket.if_indextoname()
for i in range(100):
    socket.if_indextoname(i)
# Test socket.if_nametoindex()
for i in range(100):
    socket.if_nametoindex('lo')
# Test socket.gethostbyname()
for i in range(100):
    socket.gethostbyname('localhost')
# Test socket.gethostbyname_ex()
for i in range(100):
    socket.gethostbyname_ex('localhost')
# Test socket.gethostname()
for i in range(100):
    socket.gethostname()
# Test socket.getfqdn()
for i in range(100):
    socket.getfqdn()
# Test socket.getaddrinfo()
for i in range(100):
    socket.getaddrinfo('127.0.0.1', 80, socket.AF_INET, socket.SOCK_STREAM)
# Test socket.getnameinfo()

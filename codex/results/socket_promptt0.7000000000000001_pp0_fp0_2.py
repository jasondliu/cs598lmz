import socket
# Test socket.if_indextoname()
print socket.if_indextoname(0x01)

# Test socket.if_nametoindex()
print socket.if_nametoindex('lo')

# Test socket.getaddrinfo()
print socket.getaddrinfo('localhost', 8080)

# Test socket.getnameinfo()
print socket.getnameinfo(('127.0.0.1', 8080), 0)

# Test socket.gethostbyname()
print socket.gethostbyname('localhost')
print socket.gethostbyname('localhost.localdomain')

# Test socket.gethostbyname_ex()
print socket.gethostbyname_ex('localhost')
print socket.gethostbyname_ex('localhost.localdomain')

# Test socket.gethostbyaddr()
print socket.gethostbyaddr('127.0.0.1')

# Test socket.gethostname()
print socket.gethostname()

# Test socket.getfqdn()
print socket.getfqdn('localhost')

# Test getdefaulttimeout()
print

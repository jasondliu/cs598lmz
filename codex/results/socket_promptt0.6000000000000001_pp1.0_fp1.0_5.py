import socket
# Test socket.if_indextoname()
print socket.if_indextoname(1)
# Test socket.if_nameindex()
print socket.if_nameindex()

# Test socket.gethostbyname_ex()
print socket.gethostbyname_ex('www.python.org')
print socket.gethostbyname_ex('nosuchname')

# Test socket.gethostbyaddr()
print socket.gethostbyaddr('127.0.0.1')
print socket.gethostbyaddr('::1')

# Test socket.gethostname()
print socket.gethostname()

# Test socket.gethostbyname()
print socket.gethostbyname('localhost')

# Test socket.getfqdn()
print socket.getfqdn()

# Test socket.getservbyname()
print socket.getservbyname('http')
print socket.getservbyname('http', 'tcp')
print socket.getservbyname('http', 'udp')

# Test socket.getservbyport()
print socket.getservbyport(80)
print socket

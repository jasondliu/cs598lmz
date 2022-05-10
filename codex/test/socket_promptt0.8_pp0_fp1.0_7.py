import socket
# Test socket.if_indextoname()
ind = socket.if_indextoname(1)
print(ind)
# Result: 'lo'

# Test socket.if_nameindex()
nameindex = socket.if_nameindex()
print(nameindex)
# Result: [(1, 'lo')]

# Test socket.if_nametoindex()
nametoindex = socket.if_nametoindex('lo')
print(nametoindex)
# Result: 1

# Test socket.gethostname()
host = socket.gethostname()
print(host)
# Result: ub-desktop

# Test socket.getaddrinfo()
print(socket.getaddrinfo(host,None))
# Result: [(2, 1, 6, '', ('127.0.0.1', 0)), (2, 2, 17, '', ('127.0.0.1', 0)), 
#         (2, 3, 0, '', ('127.0.0.1', 0)), (2, 4, 0, '', ('127.0.0.1', 0))]

# Test socket.get

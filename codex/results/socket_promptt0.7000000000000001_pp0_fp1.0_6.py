import socket
# Test socket.if_indextoname
if_name = socket.if_indextoname(1)
if if_name != 'lo0':
    print('ERROR: socket.if_indextoname returned incorrect name:', if_name)

# Test socket.if_nameindex
print(socket.if_nameindex())

# Test socket.getaddrinfo
ai = socket.getaddrinfo('localhost', 80, 0, 0, socket.IPPROTO_TCP)
try:
    ai = socket.getaddrinfo('localhost', 80, 0, 0, socket.IPPROTO_TCP,
                            socket.AI_CANONNAME)
except AttributeError:
    pass

# Test socket.getnameinfo
ni = socket.getnameinfo(ai[0][4], 0)
ni = socket.getnameinfo(ai[0][4], socket.NI_NUMERICSERV)
try:
    ni = socket.getnameinfo(ai[0][4], socket.NI_NUMERICSERV,
                            socket.NI_NUMERICHOST)
except AttributeError:
   

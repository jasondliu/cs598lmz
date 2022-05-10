import socket
# Test socket.if_indextoname()
print('if_indextoname(123):', socket.if_indextoname(123))
# Test socket.if_nametoindex()
print('if_nametoindex("{}"):'.format(socket.if_indextoname(123)),
      socket.if_nametoindex(socket.if_indextoname(123)))

# Test socket.getservbyname()
print('getservbyname("http"):', socket.getservbyname('http'))
# Test socket.getservbyport()
print('getservbyport(80):', socket.getservbyport(80))

# Test socket.gethostbyname()
print('gethostbyname("localhost"):', socket.gethostbyname('localhost'))
# Test socket.gethostbyname_ex()
print('gethostbyname_ex("localhost"):', socket.gethostbyname_ex('localhost'))
# Test socket.gethostname()
print('gethostname():', socket.gethostname())
# Test socket.gethostbyaddr()

import socket
# Test socket.if_indextoname
hname = socket.gethostname()
print('Hostname :', hname)
ai = socket.getaddrinfo(hname, None)[0]
print('Family :', ai[0], 'Type :', ai[1], 'Protocol:', ai[6])
# Show the address
print('Address :', ai[4][0])
# Show the interface
s = socket.socket(ai[0], ai[1], ai[6])
print('Interface :', socket.if_indextoname(socket.if_nametoindex(ai[4][0])))
# Show the interface index
print('Interface index :', socket.if_nametoindex(ai[4][0]))
# The following should all return the same
print('Raw interface index :', socket.if_nametoindex(ai[4][0]))
print('Raw interface index :', socket.if_nametoindex(ai[4][0],
  socket.if_indextoname(socket.if_nametoindex(ai[4][0]))))
# Now an invalid interface name

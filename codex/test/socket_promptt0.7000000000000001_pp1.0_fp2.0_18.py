import socket
# Test socket.if_indextoname()

[socket.if_indextoname(1), socket.if_indextoname(2)]
#['lo0', 'en0']

# Test socket.if_nameindex()

[x[0] for x in socket.if_nameindex()]
#['lo0', 'en0']

# Test socket.if_nameindex()

[x[1] for x in socket.if_nameindex()]
#[1, 2]

# Test socket.if_nametoindex()

socket.if_nametoindex('lo0')
#1

# Test socket.if_nametoindex()

socket.if_nametoindex('en0')
#2

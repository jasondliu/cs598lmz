import socket
socket.if_indextoname(4)

# 'en1'

socket.if_indextoname(4, 'eth')

# 'eth2'

socket.if_nametoindex('en1')

# 4

socket.if_nametoindex('eth2', 'eth')

# 2
</code>


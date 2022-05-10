import socket
socket.if_indextoname(3)

In [14]: socket.if_indextoname(3)
Out[14]: 'eth0'

In [15]: socket.if_nameindex()
Out[15]: [(1, 'lo'), (2, 'eth0'), (3, 'eth1')]

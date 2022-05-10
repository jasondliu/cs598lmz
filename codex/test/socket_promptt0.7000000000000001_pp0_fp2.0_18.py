import socket
# Test socket.if_indextoname compatibility with the python3 module
ifname = socket.if_indextoname(1)
assert ifname == 'lo'

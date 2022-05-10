import socket
# Test socket.if_indextoname
if_indextoname = socket.if_indextoname
if_indextoname(0, 'a')
if_indextoname(0, b'a')

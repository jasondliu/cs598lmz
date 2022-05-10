import socket
# Test socket.if_indextoname
try:
    socket.if_indextoname(1)
except (OSError, AttributeError):
    def if_indextoname(i):
        return 'lo'
else:
    if_indextoname = socket.if_indextoname

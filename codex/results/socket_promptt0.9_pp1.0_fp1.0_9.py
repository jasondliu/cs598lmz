import socket
# Test socket.if_indextoname() when interface does not exist.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    socket.if_indextoname(-100)
except ValueError:
    pass
else:
    raise Exception('socket.if_indextoname(-100) should have raised ValueError')
try:
    socket.ifa_flags(-100)
except ValueError:
    pass
else:
    raise Exception('socket.ifa_flags(-100) should have raised ValueError')

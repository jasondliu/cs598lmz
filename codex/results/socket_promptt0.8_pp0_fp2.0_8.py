import socket
# Test socket.if_indextoname()
# See http://bugs.python.org/issue1685
print(socket.if_indextoname(1))
# Check that we can read the data dictionary
print(socket.AF_APPLETALK)
print(socket.SO_REUSEPORT)
print(socket.IP_DEFAULT_MULTICAST_TTL)
print(socket.SOMAXCONN)
print(socket.SOL_SOCKET)
print(socket.SO_TYPE)

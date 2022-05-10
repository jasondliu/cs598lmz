import socket
# Test socket.if_indextoname for AF_INET and AF_INET6
print("Interface index 2 is named", socket.if_indextoname(2))
# Test socket.if_nametoindex for AF_INET and AF_INET6
print("Interface named lo is index", socket.if_nametoindex('lo'))

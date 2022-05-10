import socket
# Test socket.if_indextoname() and socket.if_indextoname()
print(socket.if_indextoname(19))
print(socket.if_nametoindex('lo'))

import socket
# Set the socket timeout
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Default socket timout: %s" %s.gettimeout())
s.settimeout(100)
print("Current socket timeout: %s" %s.gettimeout())

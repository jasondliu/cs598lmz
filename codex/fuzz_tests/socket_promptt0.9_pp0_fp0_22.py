import socket
# Test socket.if_indextoname()
try:
    print(socket.if_indextoname(1))
except OSError as e:
    print("OSError: %s" % e)

# Test socket.if_indextoname()
try:
    print(socket.if_indextoname(-1))
except OSError as e:
    print("OSError: %s" % e)

# Test socket.if_nametoindex()
try:
    i = socket.if_nametoindex("test")
    print(i)
except OSError as e:
    print("OSError: %s" % e)

try:
    i = socket.if_nametoindex("testa")
    print(i)
except OSError as e:
    print("OSError: %s" % e)

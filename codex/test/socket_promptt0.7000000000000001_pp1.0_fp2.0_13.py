import socket
# Test socket.if_indextoname()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# This returns the name of the interface corresponding to the index
print("socket.if_indextoname({})".format(s.fileno()))
print("socket.if_indextoname({})".format(s.fileno()),
      "--> {}".format(socket.if_indextoname(s.fileno())))
# This returns the index of the interface matching the name
print("socket.if_nametoindex('lo')")
print("socket.if_nametoindex('lo') --> {}".format(socket.if_nametoindex('lo')))
# This returns all the interfaces, the index and the name
print("socket.if_nameindex()")
print("socket.if_nameindex() --> {}".format(socket.if_nameindex()))
# This returns all the interfaces, the name and the addresses
# There are several addresses for the same interface
print("socket.if_nameinfo(s.getsockname(), socket.NI_NUMERICHOST)")

import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))

# Test interface name filtering
# we know the first ethernet is en0, ignore that one
for interface in  netifaces.interfaces():
    if interface[0:2] != "en":
        iface = netifaces.ifaddresses(interface)[2][0]['addr']
        print("%s: %s" % (interface,iface))

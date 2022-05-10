import socket
# Test socket.if_indextoname()
hname = socket.gethostname()
print("Host name:", hname)

try:
    iname = socket.if_indextoname(1)
except ValueError:
    iname = None
print("Interface 1:", iname)

try:
    iname = socket.if_indextoname(2)
except ValueError:
    iname = None
print("Interface 2:", iname)

try:
    iname = socket.if_indextoname(3)
except ValueError:
    iname = None
print("Interface 3:", iname)

# Convert interface name to index
print("lo =>", socket.if_nametoindex("lo"))

# Test socket.if_nameindex()
iflist = socket.if_nameindex()
for i, ifname in iflist:
    print(i, "=>", ifname)
print()

# Test socket.getaddrinfo()

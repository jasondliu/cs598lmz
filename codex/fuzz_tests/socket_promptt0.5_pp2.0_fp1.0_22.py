import socket
# Test socket.if_indextoname()

# Test with a valid interface index
ifname = socket.if_indextoname(1)
if ifname is None:
    print("Invalid interface index")
else:
    print("Interface index 1 is:", ifname)

# Test with an invalid interface index
ifname = socket.if_indextoname(1000)
if ifname is None:
    print("Invalid interface index")
else:
    print("Interface index 1000 is:", ifname)

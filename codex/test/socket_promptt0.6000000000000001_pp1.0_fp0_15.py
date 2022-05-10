import socket
# Test socket.if_indextoname
ifname = socket.if_indextoname(socket.if_nametoindex(ifname))
if ifname is None:
    raise SystemExit('socket.if_indextoname() failed')

# Get IP address of the interface
try:
    ipaddr = socket.if_indextoip(socket.if_nametoindex(ifname))
except AttributeError:
    # Python < 3.7
    ipaddr = socket.if_indextoip(socket.if_nametoindex(ifname))
if ipaddr is None:
    raise SystemExit('socket.if_indextoip() failed')

# Get the netmask
netmask = socket.if_indextomask(socket.if_nametoindex(ifname))
if netmask is None:
    raise SystemExit('socket.if_indextomask() failed')

# Get the broadcast address
try:
    broadcast = socket.if_indextobroadcast(socket.if_nametoindex(ifname))
except AttributeError:
    # Python < 3.7
    broadcast

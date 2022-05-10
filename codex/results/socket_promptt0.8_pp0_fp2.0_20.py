import socket
# Test socket.if_indextoname()
# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Get the list of valid interface names
valid_ifnames = []
for i in range(0,128):
    try:
        ifname = socket.if_indextoname(i)
        valid_ifnames.append(ifname)
    except:
        pass

# Bind the socket to the first valid interface
for ifname in valid_ifnames:
    try:
        s.bind((ifname, 0))
        break
    except:
        pass
else:
    raise ValueError("could not bind to any interface")
# Make sure socket is bound to the right interface
res = s.getsockname()[0].encode('utf-8')
ifname = socket.if_indextoname(s.fileno())
if res != ifname:
    raise ValueError("bad result %s != %s" % (res, ifname))
# Make sure socket is bound to the right interface, using if_indextoname
res = s

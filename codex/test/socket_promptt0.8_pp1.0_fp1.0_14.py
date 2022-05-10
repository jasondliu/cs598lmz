import socket
# Test socket.if_indextoname()

try:
    import ifconfig
except ImportError:
    raise ImportError("ifconfig not installed")

(ifname, ifindex) = ifconfig.ifconfig()
ifindex = int(ifindex)

try:
    name = socket.if_indextoname(ifindex)
except OSError:
    print('OSError: interface not found')
else:
    if name != ifname:
        raise Exception('test failed')

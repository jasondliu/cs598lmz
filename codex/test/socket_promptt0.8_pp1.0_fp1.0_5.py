import socket
# Test socket.if_indextoname() with IPv4
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    ifname = socket.if_indextoname(1)
    if ifname != 'lo':
        raise ValueError("Expected if_indextoname(1)=='lo', got " + ifname)
    n = socket.if_nametoindex(ifname)
    if n != 1:
        raise ValueError("Expected if_nametoindex('lo')==1, got " + n)
# Test socket.if_indextoname() with IPv6
with socket.socket(socket.AF_INET6, socket.SOCK_DGRAM) as s:
    ifname = socket.if_indextoname(1)
    if ifname != 'lo':
        raise ValueError("Expected if_indextoname(1)=='lo', got " + ifname)
    n = socket.if_nametoindex(ifname)

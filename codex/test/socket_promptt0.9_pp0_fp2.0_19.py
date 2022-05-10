import socket
# Test socket.if_indextoname:
#  - both IPv4 and IPv6 are supported
if socket.has_ipv6:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        index1 = s.if_nametoindex('lo')
        assert socket.if_indextoname(index1) == 'lo'
        index2 = s.if_nametoindex('lo')
        assert socket.if_indextoname(index2) == 'lo'
        assert index1 == index2
    with socket.socket(socket.AF_INET6, socket.SOCK_DGRAM) as s:
        index3 = s.if_nametoindex('lo')
        assert socket.if_indextoname(index3) == 'lo'

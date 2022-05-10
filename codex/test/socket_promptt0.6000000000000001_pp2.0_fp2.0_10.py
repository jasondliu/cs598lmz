import socket
# Test socket.if_indextoname
#

def test(family):
    ifname = socket.if_indextoname(1)
    if ifname != 'lo':
        raise ValueError('if_indextoname(1) = %s, expected "lo"' % ifname)

    index = socket.if_nametoindex(ifname)
    if index != 1:
        raise ValueError('if_nametoindex(lo) = %d, expected 1' % index)

test(socket.AF_INET)
test(socket.AF_INET6)

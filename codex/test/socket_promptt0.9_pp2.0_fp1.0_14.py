import socket
# Test socket.if_indextoname and socket.if_nametoindex
# on all interfaces.

def hex_addr(s):
    h = ""
    for c in s:
        h = h + '%02x' % (ord(c),)
    return h
def test_if(name):
    i = socket.if_nametoindex(name)

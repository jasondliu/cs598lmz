import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    if ifname != 'lo' and ifname != 'lo0':
        raise TestFailed("socket.if_indextoname(1) returned %s, expected 'lo' or 'lo0'" % repr(ifname))

# Test socket.if_nameindex()

def test_if_nameindex():
    # The result of socket.if_nameindex() should be a list of (index, name)
    # tuples.
    for index, name in socket.if_nameindex():
        ifname = socket.if_indextoname(index)
        if ifname != name:
            raise TestFailed("socket.if_indextoname(%d) returned %s, expected %s" % (index, repr(ifname), repr(name)))

# Test socket.if_nametoindex()

def test_if_nametoindex():
    ifindex = socket.if_nametoindex('lo')

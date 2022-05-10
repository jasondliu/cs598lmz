import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    print ifname
    assert ifname == 'lo'

# Test socket.if_indextoname()

def test_if_nametoindex():
    ifindex = socket.if_nametoindex(ifname)
    print ifindex
    assert ifindex == 1

# Test socket.if_nameindex()

def test_if_nameindex():
    ifindexes = socket.if_nameindex()
    print ifindexes
    assert ifindexes[0] == (1, 'lo')

# Test socket.if_nameindex()

def test_if_nameindex():
    ifindexes = socket.if_nameindex()
    print ifindexes
    assert ifindexes[0] == (1, 'lo')

# Test socket.if_nameindex()

def test_if_nameindex():
    ifindexes = socket.if_nameindex()
    print ifindexes
    assert ifindexes[0

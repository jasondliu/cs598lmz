import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(0)
    if not ifname:
        raise TestFailed, "no interface with index 0"

# Test socket.if_nameindex()

def test_if_nameindex():
    names = socket.if_nameindex()
    if not names:
        raise TestFailed, "no interfaces"

# Test socket.if_nameindex()

def test_if_nametoindex():
    names = socket.if_nameindex()
    if not names:
        raise TestFailed, "no interfaces"

    for ifname, ifindex in names:
        ifindex2 = socket.if_nametoindex(ifname)
        if ifindex != ifindex2:
            raise TestFailed, "if_nametoindex() returned wrong value"

    try:
        ifindex = socket.if_nametoindex("pypypypypypypypypypypy");
    except socket.error:
        pass
    else:
        raise TestFailed

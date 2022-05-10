import socket
# Test socket.if_indextoname()
if_indextoname = socket.if_indextoname

def test_if_indextoname():
    # This test is only valid on systems with at least one network interface
    # and where the first network interface has a name.
    ifname = if_indextoname(1)
    if ifname is not None:
        assert if_indextoname(if_nametoindex(ifname)) == ifname
    else:
        py.test.skip("no network interface")

# Test socket.if_nameindex()
if_nameindex = socket.if_nameindex

def test_if_nameindex():
    # This test is only valid on systems with at least one network interface
    # and where the first network interface has a name.
    ifname = if_indextoname(1)
    if ifname is not None:
        assert if_nameindex()[0][1] == if_nametoindex(ifname)
    else:
        py.test.skip("no network interface")

# Test socket.if_nameindex()


import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    """
    Test socket.if_indextoname()
    """
    # Get the list of interfaces
    ifaces = socket.if_nameindex()
    for iface in ifaces:
        # Get the interface name from the index
        ifname = socket.if_indextoname(iface[0])
        # Check that the name is valid
        if ifname is not None:
            # Check that the index is valid
            ifindex = socket.if_nametoindex(ifname)
            assert ifindex == iface[0]

def test_if_nameindex():
    """
    Test socket.if_nameindex()
    """
    # Get the list of interfaces
    ifaces = socket.if_nameindex()
    for iface in ifaces:
        # Get the interface index from the name
        ifindex = socket.if_nametoindex(iface[1])
        # Check that the index is valid

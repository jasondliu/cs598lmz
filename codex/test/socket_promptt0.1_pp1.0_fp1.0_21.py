import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    ifname = socket.if_indextoname(1)
    if ifname is None:
        raise TestFailed("if_indextoname(1) returned None")
    if ifname not in socket.if_nameindex():
        raise TestFailed("if_indextoname(1) returned an unknown interface")

def test_if_nameindex():
    # Test if_nameindex()
    nics = socket.if_nameindex()
    if len(nics) == 0:
        raise TestFailed("if_nameindex() returned no interfaces")
    for i,nic in enumerate(nics):
        name,index = nic
        if index != i:
            raise TestFailed("if_nameindex() returned wrong index for %s" % name)

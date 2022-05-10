import socket
# Test socket.if_indextoname()
ifaces = socket.if_nameindex()
for iface in ifaces:
    idx, name = iface
    assert isinstance(idx, int)

    # these seem to be common, so we have to check for their existence
    # separately.  e.g. lo and eth0.
    # pylint: disable=E1101
    if idx in socket.if_nametoindex.registry:
        assert name == socket.if_indextoname(idx)
        assert idx == socket.if_nametoindex(name)
    # pylint: enable=E1101

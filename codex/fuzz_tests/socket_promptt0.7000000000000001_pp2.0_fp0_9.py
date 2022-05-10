import socket
# Test socket.if_indextoname()
#
#   if_indextoname() converts an interface index to the corresponding
#   name.  If the index is invalid, it returns an empty string.

def test(family):
    print("Testing if_indextoname() with family %s" % {
        socket.AF_INET: "AF_INET",
        socket.AF_INET6: "AF_INET6",
    }.get(family, "unknown family"))

    # Get the interfaces that are up on the system.
    ifaces = [i[1] for i in socket.if_nameindex() if i[0] != 0]

    for iface in ifaces:
        index = socket.if_nametoindex(iface)
        name = socket.if_indextoname(index)
        print("  %-12s -> %2d -> %-12s" % (iface, index, name))

    # Try with a bogus index.
    try:
        name = socket.if_indextoname(-1)
        print("  Bogus index unexpectedly succeeded:

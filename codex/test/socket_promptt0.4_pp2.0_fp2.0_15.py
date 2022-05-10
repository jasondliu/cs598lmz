import socket
# Test socket.if_indextoname()
import socket
import sys

# This is a list of all the interfaces on the system.
# It is used to test if the interface name is valid.
interfaces = [i[1] for i in socket.if_nameindex()]

def test(ifname):
    try:
        # Convert the interface name to an index.
        ifindex = socket.if_nametoindex(ifname)
    except OSError:
        # The interface name is invalid.
        print(f"{ifname!r} is not a valid interface name on this system")
        return

    try:
        # Convert the index back to an interface name.
        ifname2 = socket.if_indextoname(ifindex)
    except OSError:
        # The index is invalid.
        print(f"{ifindex} is not a valid interface index on this system")
        return

    # Compare the original interface name with the one
    # returned by if_indextoname().

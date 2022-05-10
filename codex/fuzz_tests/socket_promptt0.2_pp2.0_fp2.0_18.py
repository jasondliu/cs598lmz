import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    #
    # This test is not very good, as it relies on the network configuration
    # of the machine running the test.
    #
    # It assumes that the machine has at least one interface, and that
    # the interface has an address.
    #
    # It also assumes that the interface has a name of the form 'ethX' or
    # 'lo', where X is a number.
    #
    # It also assumes that the interface has an index less than 2**16.

    # Get all addresses on all interfaces
    addrs = socket.getaddrinfo(None, 0, socket.AF_UNSPEC, socket.SOCK_STREAM,
                               0, socket.AI_PASSIVE)

    # Find the index of the first interface that has an address
    for a in addrs:
        if a[4][0] != '127.0.0.1':
            index = a[4][-1]
            break
    else:
        raise RuntimeError("No

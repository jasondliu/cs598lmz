import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Get the interface table
    ifaces = socket.if_nameindex()
    # Check that if_indextoname() works for all interfaces
    for i in ifaces:
        try:
            socket.if_indextoname(i[0])
        except ValueError:
            print("if_indextoname(%d) failed" % i[0])

test_if_indextoname()

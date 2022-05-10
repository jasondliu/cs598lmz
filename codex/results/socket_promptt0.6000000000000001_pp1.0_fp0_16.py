import socket
# Test socket.if_indextoname()
# Note, this test requires the system has at least two interfaces.

def test_if_indextoname():
    # get an interface index by its name
    name = socket.if_indextoname(socket.if_nametoindex('lo'))
    assert name == 'lo', name

    # get an interface index by its name
    name = socket.if_indextoname(socket.if_nametoindex('eth0'))
    assert name == 'eth0', name

    # invalid interface index
    raises(ValueError, socket.if_indextoname, -1)
    raises(ValueError, socket.if_indextoname, 0)
    raises(ValueError, socket.if_indextoname, 2**31-1)
    raises(ValueError, socket.if_indextoname, 2**32)

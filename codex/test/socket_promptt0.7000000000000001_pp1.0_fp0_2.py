import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    try:
        socket.if_indextoname(1)
    except socket.error:
        pass
    else:
        assert False, 'invalid interface name not detected'

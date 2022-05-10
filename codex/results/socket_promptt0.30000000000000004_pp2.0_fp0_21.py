import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # This test is only meaningful on systems that support the SIOCGIFNAME ioctl.
    # On other systems, this function always returns None.
    if hasattr(socket, 'SIOCGIFNAME'):
        assert socket.if_indextoname(1) in ('lo', 'lo0')
    else:
        assert socket.if_indextoname(1) is None

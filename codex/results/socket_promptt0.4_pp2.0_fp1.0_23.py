import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    if not hasattr(socket, 'if_indextoname'):
        skip('if_indextoname() not available')
    ifname = socket.if_indextoname(1)
    if not ifname:
        skip('if_indextoname() returned empty string')
    assert socket.if_indextoname(1) == ifname
    assert socket.if_indextoname(1) == ifname
    assert socket.if_indextoname(1) == ifname
    assert socket.if_indextoname(1) == ifname
    assert socket.if_indextoname(1) == ifname
    assert socket.if_indextoname(1) == ifname
    assert socket.if_indextoname(1) == ifname
    assert socket.if_indextoname(1) == ifname
    assert socket.if_indextoname(1) == ifname
    assert socket.if_indextoname(1) == ifname
   

import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    assert socket.if_indextoname(1) == 'lo'
    assert socket.if_indextoname(2) == 'eth0'
    try:
        socket.if_indextoname(3)
    except OSError:
        pass
    else:
        raise Exception('expected OSError')

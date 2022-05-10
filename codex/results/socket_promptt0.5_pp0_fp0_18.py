import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    assert socket.if_indextoname(1) == 'lo'
    try:
        socket.if_indextoname(999999)
    except ValueError as e:
        assert 'invalid network interface index' in str(e)
    else:
        assert False, 'Expected ValueError'

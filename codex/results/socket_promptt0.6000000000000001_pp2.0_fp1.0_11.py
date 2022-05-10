import socket
# Test socket.if_indextoname

def test_if_indextoname():
    """Test socket.if_indextoname"""
    try:
        socket.if_indextoname(0)
    except AttributeError:
        pass
    else:
        assert False, 'socket.if_indextoname should not exist'

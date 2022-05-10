import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    try:
        socket.if_indextoname(1)
    except ValueError:
        pass
    else:
        assert False, 'expected ValueError'

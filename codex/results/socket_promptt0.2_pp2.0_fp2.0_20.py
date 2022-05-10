import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    try:
        socket.if_indextoname(1)
    except OSError:
        pass
    else:
        raise Exception('expected OSError')

test_if_indextoname()

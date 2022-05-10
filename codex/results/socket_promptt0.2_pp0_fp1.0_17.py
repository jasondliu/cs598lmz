import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    try:
        socket.if_indextoname(1)
    except socket.error as e:
        if e.errno != errno.ENXIO:
            raise
    else:
        raise Exception("Expected socket.error")

test_if_indextoname()

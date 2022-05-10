import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    try:
        socket.if_indextoname(1)
    except OSError as e:
        if e.args[0] != errno.ENXIO:
            raise
    else:
        raise Exception("Expected OSError")

test_if_indextoname()

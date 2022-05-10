import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    try:
        socket.if_indextoname(0)
    except socket.error:
        pass
    else:
        raise RuntimeError("Expected socket.error")

test_if_indextoname()

import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # test error conditions
    try:
        socket.if_indextoname(-1)
    except ValueError:
        pass

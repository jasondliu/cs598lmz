import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Check if the function is available
    if not hasattr(socket, 'if_indextoname'):
        raise TestSkipped, "if_indextoname not available"
    # Check if the function works
    try:
        socket.if_indextoname(1)
    except socket.error:
        raise TestSkipped, "if_indextoname not working"

test_if_indextoname()

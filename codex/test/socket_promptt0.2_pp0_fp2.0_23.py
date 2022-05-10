import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    if_indextoname = socket.if_indextoname
    # Test with invalid index
    try:
        if_indextoname(-1)
    except ValueError:
        pass
    else:
        raise Exception('if_indextoname(-1) should have raised ValueError')
    # Test with valid index
    if_indextoname(1)


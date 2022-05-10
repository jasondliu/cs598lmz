import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    """Test if_indextoname()."""
    try:
        socket.if_indextoname(1)
    except socket.error:
        pass
    else:
        print("if_indextoname() without a valid index should have failed")

    try:
        socket.if_indextoname(-1)
    except socket.error:
        pass
    else:
        print("if_indextoname() with a negative index should have failed")

    try:
        socket.if_indextoname(0xFFFFFFFF)
    except socket.error:
        pass
    else:
        print("if_indextoname() with a negative index should have failed")

    if not socket.if_indextoname(0):
        print("if_indextoname() with an index of zero returned None")

if __name__ == "__main__":
    test_if_indextoname()

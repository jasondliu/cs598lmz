import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    """
    Test socket.if_indextoname()
    """
    if_indextoname = socket.if_indextoname
    try:
        if_indextoname(0)
    except ValueError:
        pass
    else:
        raise Exception("if_indextoname(0) should fail")
    try:
        if_indextoname(-1)
    except ValueError:
        pass
    else:
        raise Exception("if_indextoname(-1) should fail")
    try:
        if_indextoname(1)
    except ValueError:
        pass
    else:
        raise Exception("if_indextoname(1) should fail")

if __name__ == '__main__':
    test_if_indextoname()

import socket
# Test socket.if_indextoname() function

def test(args):
    """Test if_indextoname() function.

    socket.if_indextoname() returns the interface name for the given numeric index.

    """
    try:
        res = socket.if_indextoname(0)
    except:
        raise socket.error("Cannot get interface name")
    assert res

    try:
        res = socket.if_indextoname(-1)
    except:
        pass
    else:
        raise socket.error("Invalid interface index")

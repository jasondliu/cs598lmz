import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # test invalid index
    try:
        socket.if_indextoname(-1)
    except ValueError:
        pass
    else:
        raise Exception("if_indextoname(-1) should have raised ValueError")

    # test valid index
    ifname = socket.if_indextoname(1)
    if ifname is None:
        raise Exception("if_indextoname(1) should not have returned None")

# Test socket.if_nameindex()

def test_if_nameindex():
    # test invalid index
    try:
        socket.if_nameindex(-1)
    except ValueError:
        pass
    else:
        raise Exception("if_nameindex(-1) should have raised ValueError")

    # test valid index
    ifname = socket.if_nameindex(1)
    if ifname is None:
        raise Exception("if_nameindex(1) should not have returned None")

# Test socket.if_nametoindex()

def test_

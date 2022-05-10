import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    try:
        socket.if_indextoname(0)
    except socket.error:
        pass
    else:
        raise TestFailed("if_indextoname() failed to raise socket.error")

    try:
        socket.if_indextoname(-1)
    except socket.error:
        pass
    else:
        raise TestFailed("if_indextoname() failed to raise socket.error")

    try:
        socket.if_indextoname(1<<32)
    except socket.error:
        pass
    else:
        raise TestFailed("if_indextoname() failed to raise socket.error")

    name = socket.if_indextoname(1)
    if not name:
        raise TestFailed("if_indextoname() returned empty string")

def test_if_nameindex():
    idx = socket.if_nametoindex("lo")
    if idx != 1:
        raise TestFailed("if_nametoindex

import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # This test is not portable.
    ifname = socket.if_indextoname(1)
    assert ifname == 'lo'

def test_if_indextoname_error():
    try:
        socket.if_indextoname(-1)
    except ValueError:
        pass
    else:
        assert False, 'expected ValueError'

def test_if_indextoname_error2():
    try:
        socket.if_indextoname(socket.if_nametoindex('lo') + 1)
    except ValueError:
        pass
    else:
        assert False, 'expected ValueError'

def test_if_indextoname_error3():
    try:
        socket.if_indextoname(0)
    except ValueError:
        pass
    else:
        assert False, 'expected ValueError'

def test_if_indextoname_error4():
    try:
        socket.if_indextoname(0xFFFF

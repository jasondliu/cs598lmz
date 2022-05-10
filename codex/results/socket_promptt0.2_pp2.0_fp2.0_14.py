import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    assert ifname == 'lo'

def test_if_indextoname_error():
    try:
        socket.if_indextoname(0)
    except OSError as e:
        assert e.args[0] == errno.EINVAL
    else:
        assert False, 'OSError not raised'

def test_if_indextoname_error2():
    try:
        socket.if_indextoname(1000000)
    except OSError as e:
        assert e.args[0] == errno.EINVAL
    else:
        assert False, 'OSError not raised'

# Test socket.if_nameindex()

def test_if_nameindex():
    ifs = socket.if_nameindex()
    assert ifs[0][0] == 1
    assert ifs[0][1] == 'lo'

# Test socket.if_nametoindex()

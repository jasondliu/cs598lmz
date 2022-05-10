import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # This test is only meaningful on platforms with at least one network
    # interface
    if not socket.if_nameindex():
        return
    # This test is only meaningful on platforms with at least one network
    # interface
    if not socket.if_nameindex():
        return
    for index, name in socket.if_nameindex():
        assert socket.if_indextoname(index) == name

def test_if_nameindex():
    nameindex = socket.if_nameindex()
    assert isinstance(nameindex, list)
    for index, name in nameindex:
        assert isinstance(index, int)
        assert isinstance(name, str)
        assert socket.if_indextoname(index) == name

def test_if_nameindex_errors():
    try:
        socket.if_nameindex(-1)
    except ValueError:
        pass
    else:
        raise AssertionError

def test_if_nametoindex():
    # This test is only meaningful on

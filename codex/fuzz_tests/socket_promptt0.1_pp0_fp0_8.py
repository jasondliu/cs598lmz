import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    ifname = socket.if_indextoname(1)
    assert ifname == 'lo'

def test_if_indextoname_error():
    # Test if_indextoname() with invalid index
    with pytest.raises(OSError):
        socket.if_indextoname(0)

def test_if_indextoname_error2():
    # Test if_indextoname() with invalid index
    with pytest.raises(OSError):
        socket.if_indextoname(2)

def test_if_indextoname_error3():
    # Test if_indextoname() with invalid index
    with pytest.raises(OSError):
        socket.if_indextoname(3)

def test_if_indextoname_error4():
    # Test if_indextoname() with invalid index
    with pytest.raises(OSError):
        socket.

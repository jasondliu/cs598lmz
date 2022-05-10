import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    assert ifname == 'lo'

def test_if_indextoname_exception():
    with pytest.raises(OSError):
        socket.if_indextoname(0)

def test_if_indextoname_exception_2():
    with pytest.raises(OSError):
        socket.if_indextoname(2)

def test_if_indextoname_exception_3():
    with pytest.raises(OSError):
        socket.if_indextoname(3)

def test_if_indextoname_exception_4():
    with pytest.raises(OSError):
        socket.if_indextoname(4)

def test_if_indextoname_exception_5():
    with pytest.raises(OSError):
        socket.if_indextoname(5)

def test_if_indext

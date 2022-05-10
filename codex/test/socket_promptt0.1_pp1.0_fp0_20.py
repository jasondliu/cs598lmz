import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    assert socket.if_indextoname(1) == 'lo'

def test_if_indextoname_error():
    with pytest.raises(OSError):
        socket.if_indextoname(0)

def test_if_indextoname_error_2():
    with pytest.raises(OSError):
        socket.if_indextoname(2)

def test_if_indextoname_error_3():
    with pytest.raises(OSError):
        socket.if_indextoname(3)

def test_if_indextoname_error_4():
    with pytest.raises(OSError):
        socket.if_indextoname(4)

def test_if_indextoname_error_5():
    with pytest.raises(OSError):
        socket.if_indextoname(5)


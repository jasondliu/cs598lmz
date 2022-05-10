import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    assert ifname == 'lo'

def test_if_indextoname_invalid():
    with pytest.raises(OSError):
        socket.if_indextoname(9999)

def test_if_indextoname_invalid_type():
    with pytest.raises(TypeError):
        socket.if_indextoname('1')

def test_if_indextoname_invalid_type_None():
    with pytest.raises(TypeError):
        socket.if_indextoname(None)

def test_if_indextoname_invalid_type_float():
    with pytest.raises(TypeError):
        socket.if_indextoname(1.1)

def test_if_indextoname_invalid_type_bool():
    with pytest.raises(TypeError):
        socket.if_indextoname(True)


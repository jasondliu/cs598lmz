import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    if_index = socket.if_nametoindex('lo')
    if_name = socket.if_indextoname(if_index)
    assert if_name == 'lo'

def test_if_indextoname_error():
    # Test if_indextoname() errors
    with pytest.raises(OSError):
        socket.if_indextoname(0)
    with pytest.raises(OSError):
        socket.if_indextoname(-1)
    with pytest.raises(OSError):
        socket.if_indextoname(1000000)

def test_if_indextoname_type():
    # Test if_indextoname() type
    with pytest.raises(TypeError):
        socket.if_indextoname('lo')
    with pytest.raises(TypeError):
        socket.if_indextoname(None)

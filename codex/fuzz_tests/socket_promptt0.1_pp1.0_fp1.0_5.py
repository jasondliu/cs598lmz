import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    ifname = socket.if_indextoname(1)
    assert ifname == 'lo'

def test_if_indextoname_invalid():
    # Test if_indextoname() with invalid index
    with pytest.raises(OSError):
        socket.if_indextoname(0)

def test_if_indextoname_non_integer():
    # Test if_indextoname() with non-integer index
    with pytest.raises(TypeError):
        socket.if_indextoname('1')

def test_if_indextoname_non_string():
    # Test if_indextoname() with non-string index
    with pytest.raises(TypeError):
        socket.if_indextoname(1.0)

def test_if_indextoname_non_string():
    # Test if_indextoname() with non-string index
    with py

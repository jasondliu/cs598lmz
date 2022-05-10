import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    assert socket.if_indextoname(1) == 'lo'

def test_if_indextoname_exception():
    with pytest.raises(OSError):
        socket.if_indextoname(100)

def test_if_indextoname_exception_msg():
    with pytest.raises(OSError) as excinfo:
        socket.if_indextoname(100)
    assert "interface index not found" in str(excinfo.value)

def test_if_indextoname_exception_errno():
    with pytest.raises(OSError) as excinfo:
        socket.if_indextoname(100)
    assert excinfo.value.errno == errno.EINVAL

def test_if_indextoname_exception_errno_msg():
    with pytest.raises(OSError) as excinfo:
        socket.if_indextoname(100)
    assert excinfo.value.

import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    """
    Test socket.if_indextoname()
    """
    # Get the interface name of the loopback interface
    if_name = socket.if_indextoname(1)
    assert if_name == 'lo'

def test_if_indextoname_error():
    """
    Test socket.if_indextoname() with invalid index
    """
    # Get the interface name of the loopback interface
    try:
        socket.if_indextoname(0)
    except socket.error as e:
        assert e.errno == errno.EINVAL

def test_if_indextoname_error2():
    """
    Test socket.if_indextoname() with invalid index
    """
    # Get the interface name of the loopback interface
    try:
        socket.if_indextoname(65536)
    except socket.error as e:
        assert e.errno == errno.EINVAL

import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    assert ifname == 'lo'

def test_if_indextoname_error():
    try:
        socket.if_indextoname(0)
    except OSError as e:
        assert e.errno == errno.EINVAL

def test_if_indextoname_error_string():
    try:
        socket.if_indextoname('1')
    except TypeError as e:
        assert str(e) == "if_indextoname() argument 1 must be int, not str"

def test_if_indextoname_error_negative():
    try:
        socket.if_indextoname(-1)
    except OSError as e:
        assert e.errno == errno.EINVAL


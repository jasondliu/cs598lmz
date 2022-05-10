import socket
# Test socket.if_indextoname
def test_EDS_SOCKET_05():
    assert socket.if_indextoname(socket.if_nametoindex('lo')) == 'lo'

# Test socket.getsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY)
def test_EDS_SOCKET_06():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        assert sock.getsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY) == 0
    except:
        assert False

# Test socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
# Test socket.getsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY)

import socket
# Test socket.if_indextoname


def test_socket_if_indextoname():
    index = 1
    ipstr = '127.0.0.1'

    # create UDP socket with 'index'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, index)

    # try 'fake' index
    pytest.raises(OSError, socket.if_indextoname, index + 100)
    assert sock.fileno() == os.dup(sock.fileno())
    assert socket.if_indextoname(index) == socket.if_indextoname(index)
    os.close(sock.fileno())

    sock.close()
    sock = None

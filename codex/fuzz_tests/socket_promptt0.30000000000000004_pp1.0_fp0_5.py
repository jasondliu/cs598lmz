import socket
# Test socket.if_indextoname()

# Test socket.if_indextoname()

def test_socket_if_indextoname(dev):
    """
    Test socket.if_indextoname()
    """
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
    sock.bind((dev, 0))
    ifname = sock.if_indextoname(sock.getsockname()[4])
    sock.close()
    assert ifname == dev, "socket.if_indextoname() failed"

if __name__ == "__main__":
    test_socket_if_indextoname(sys.argv[1])

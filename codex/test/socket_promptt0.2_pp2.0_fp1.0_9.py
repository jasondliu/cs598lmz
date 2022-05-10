import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    try:
        socket.if_indextoname(1)
    except OSError as e:
        if e.errno == errno.ENXIO:
            print("No such network interface")
        else:
            raise
    else:
        print("Network interface name:", socket.if_indextoname(1))

if __name__ == '__main__':
    test_if_indextoname()

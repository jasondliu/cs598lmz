import socket
# Test socket.if_indextoname()

if_indextoname = socket.if_indextoname

def test_if_indextoname():
    # Test if_indextoname()
    try:
        if_indextoname(1)
    except OSError as e:
        if e.errno != errno.ENXIO:
            raise
    else:
        raise RuntimeError("if_indextoname(1) didn't raise ENXIO")

if __name__ == '__main__':
    test_if_indextoname()

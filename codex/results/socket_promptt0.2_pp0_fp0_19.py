import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    try:
        socket.if_indextoname(1)
    except OSError as e:
        if e.errno == errno.ENXIO:
            print("SKIP")
            raise unittest.SkipTest("if_indextoname() not supported")
        raise
    print("PASS")

test_if_indextoname()

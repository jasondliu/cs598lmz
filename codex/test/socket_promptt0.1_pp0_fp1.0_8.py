import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    try:
        socket.if_indextoname(1)
    except OSError as e:
        if e.errno != errno.EINVAL:
            raise
    else:
        raise Exception("if_indextoname() should fail with EINVAL")

    try:
        socket.if_indextoname(0xffffffff)
    except OSError as e:
        if e.errno != errno.EINVAL:
            raise
    else:
        raise Exception("if_indextoname() should fail with EINVAL")

    try:
        socket.if_indextoname(-1)
    except OSError as e:
        if e.errno != errno.EINVAL:
            raise
    else:
        raise Exception("if_indextoname() should fail with EINVAL")


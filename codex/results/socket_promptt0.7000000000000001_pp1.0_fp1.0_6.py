import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    try:
        socket.if_indextoname(1)
    except OSError as e:
        if e.errno != errno.ENXIO:
            raise
    else:
        assert False, "Expected OSError"

def test_if_indextoname2():
    try:
        socket.if_indextoname(1, 1)
    except OSError as e:
        if e.errno != errno.EINVAL:
            raise
    else:
        assert False, "Expected OSError"

def test_if_indextoname3():
    socket.if_indextoname(0)

def test_if_indextoname4():
    try:
        socket.if_indextoname(1, 0)
    except OSError as e:
        if e.errno != errno.ENXIO:
            raise
    else:
        assert False, "Expected OSError"

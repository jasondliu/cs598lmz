import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    if ifname != 'lo':
        raise Exception("if_indextoname(1) returned '%s' instead of 'lo'" % ifname)

def test_if_indextoname_error():
    try:
        socket.if_indextoname(0)
    except OSError:
        pass
    else:
        raise Exception("if_indextoname(0) didn't raise OSError")

def test_if_indextoname_error2():
    try:
        socket.if_indextoname(100000)
    except OSError:
        pass
    else:
        raise Exception("if_indextoname(100000) didn't raise OSError")

def test_if_indextoname_error3():
    try:
        socket.if_indextoname(-1)
    except OSError:
        pass
    else:
        raise

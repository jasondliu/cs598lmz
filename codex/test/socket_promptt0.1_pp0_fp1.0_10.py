import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    if_indextoname = socket.if_indextoname
    try:
        if_indextoname(0)
    except ValueError:
        pass
    else:
        raise Exception("if_indextoname(0) should raise ValueError")
    try:
        if_indextoname(-1)
    except ValueError:
        pass
    else:
        raise Exception("if_indextoname(-1) should raise ValueError")
    try:
        if_indextoname(1<<32)
    except ValueError:
        pass
    else:
        raise Exception("if_indextoname(1<<32) should raise ValueError")
    try:
        if_indextoname(1<<31)
    except ValueError:
        pass
    else:
        raise Exception("if_indextoname(1<<31) should raise ValueError")
    try:
        if_indextoname(1<<30)
    except ValueError:
        pass

import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    try:
        socket.if_indextoname(1)
    except:
        pass
    else:
        raise Exception("if_indextoname() should have failed")

    try:
        socket.if_indextoname(1, "foo")
    except:
        pass
    else:
        raise Exception("if_indextoname() should have failed")

    try:
        socket.if_indextoname(1, "foo", "bar")
    except:
        pass
    else:
        raise Exception("if_indextoname() should have failed")

    try:
        socket.if_indextoname(1, "foo", "bar", "baz")
    except:
        pass
    else:
        raise Exception("if_indextoname() should have failed")

    try:
        socket.if_indextoname(1, "foo", "bar", "baz", "qux")
    except:
        pass

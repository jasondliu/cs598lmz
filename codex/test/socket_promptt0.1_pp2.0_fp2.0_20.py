import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    try:
        socket.if_indextoname(1)
    except socket.error:
        pass
    else:
        raise Exception("if_indextoname() should have failed")

def test_if_indextoname_2():
    # Test if_indextoname()
    try:
        socket.if_indextoname(1)
    except socket.error:
        pass
    else:
        raise Exception("if_indextoname() should have failed")

def test_if_indextoname_3():
    # Test if_indextoname()
    try:
        socket.if_indextoname(1)
    except socket.error:
        pass
    else:
        raise Exception("if_indextoname() should have failed")


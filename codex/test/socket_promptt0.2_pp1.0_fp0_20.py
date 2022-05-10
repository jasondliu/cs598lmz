import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    """
    Test socket.if_indextoname()
    """
    try:
        socket.if_indextoname(1)
    except socket.error:
        pass
    else:
        raise Exception("socket.if_indextoname() should fail")

def test_if_indextoname_exception():
    """
    Test socket.if_indextoname() exception
    """
    try:
        socket.if_indextoname(1)
    except socket.error:
        pass
    else:
        raise Exception("socket.if_indextoname() should fail")

def test_if_indextoname_exception_with_message():
    """
    Test socket.if_indextoname() exception with message
    """

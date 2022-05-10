import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # test if_indextoname()
    try:
        socket.if_indextoname(1)
    except socket.error:
        pass
    else:
        raise Exception("if_indextoname() should have failed")

test_if_indextoname()

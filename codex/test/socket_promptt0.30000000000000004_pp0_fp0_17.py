import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    try:
        socket.if_indextoname(1)
    except:
        pass
    else:
        raise Exception("if_indextoname() should fail on Windows")

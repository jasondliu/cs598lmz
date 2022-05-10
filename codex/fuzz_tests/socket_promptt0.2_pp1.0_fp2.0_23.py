import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    if ifname != "lo":
        raise Exception("if_indextoname() failed")

test_if_indextoname()

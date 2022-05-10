import socket
# Test socket.if_indextoname()

def test(ifindex):
    try:
        name = socket.if_indextoname(ifindex)
    except ValueError:
        name = None

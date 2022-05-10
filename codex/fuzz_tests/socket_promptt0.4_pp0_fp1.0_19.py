import socket
# Test socket.if_indextoname()

def test(family):
    try:
        if_indextoname(family, 1)
    except OSError:
        pass

test(socket.AF_INET)
test(socket.AF_INET6)

import socket
# Test socket.if_indextoname()

def test(family):
    try:
        socket.if_indextoname(1, family)
    except (OSError, ValueError):
        pass
    else:
        print(family, 'failed')

test(socket.AF_INET)
test(socket.AF_INET6)

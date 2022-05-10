import socket
# Test socket.if_indextoname()

def if_indextoname(ifindex):
    for i, n in (socket.if_nameindex()):
        if i == ifindex:
            return n

def test_if_indextoname():
    socket.if_indextoname(if_indextoname(socket.if_nametoindex(
        'lo'))) == 'lo'

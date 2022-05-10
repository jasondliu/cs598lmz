import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    socket.if_indextoname(1)
    socket.if_indextoname(1, 'foo')

try:
    socket.if_indextoname(1, 'foo', 'bar')
except TypeError:
    pass
